from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    """
    This class is used to customize the user
    registration form for the User model class.
    Django form to get user details for login/
    logout information.
    """

    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Email"}),
    )
    password1 = forms.CharField(
        label="Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )
    password2 = forms.CharField(
        label="Retype Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class AuthForm(AuthenticationForm):
    """
    Form that uses built-in AuthenticationForm to handle user auth
    """

    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )

    class Meta:
        model = User
        fields = ["username", "password"]
