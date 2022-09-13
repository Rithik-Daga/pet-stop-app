from . import models
from django.views import View
from django.conf import settings
from django.contrib import messages
from .forms import AuthForm, SignUpForm
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.tokens import default_token_generator

# Create your views here.
def signinView(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = AuthForm()
    if request.method == "POST":
        forward_url = request.GET.get("next", "/community/global-feed/")
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            messages.success(request, f"welcome back, {user}!")
        else:
            messages.error(request, "Username/Password is incorrect.")
        return redirect(forward_url)

    context = {"form": form}
    return render(request, "users/signin.html", context=context)


def signoutView(request):

    logout(request)
    messages.success(request, "Logout successful!")
    return redirect("signin")


def profileView(request):
    user_profile = models.UserProfile.objects.get(user=request.user)
    context = {"user_profile": user_profile}
    return render(request, "users/profile.html", context=context)


class SignUpView(View):

    form_class = SignUpForm
    template_name = "users/signup.html"

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("signin")
        else:
            messages.error(request, "Account couldn't be created.")
        context = {"form": form}
        return render(request, self.template_name, context=context)


class PasswordResetRequestView(View):

    form_class = PasswordResetForm
    template_name = "users/password/password_reset.html"
    subject = "Password Reset Requested"
    email_template_name = "users/password/password_reset_email.txt"

    def get(self, request):
        context = {"password_reset_form": self.form_class}
        return render(request, self.template_name, context=context)

    def post(self, request):

        password_reset_form = self.form_class(request.POST)
        if password_reset_form.is_valid():
            email_id = password_reset_form.cleaned_data["email"]

            try:
                user = User.objects.get(email=email_id)
            except User.DoesNotExist:
                return HttpResponse("Email not found.")

            self.send_reset_email(user)

        return redirect("password_reset_done")

    def send_reset_email(self, user: User):
        email_context = {
            "email": user.email,
            "domain": settings.DOMAIN,
            "site_name": settings.SITE_NAME,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            "protocol": "http",
            "token": default_token_generator.make_token(user),
        }

        print("\n\n", email_context, "\n\n")
        email = render_to_string(self.email_template_name, context=email_context)
        try:
            send_mail(
                self.subject,
                email,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")

        return
