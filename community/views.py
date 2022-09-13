from . import models
from django.shortcuts import render, redirect
from users import models as user_models
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="signin")
def globalFeed(request):
    posts = user_models.ProfilePosts.objects.all()  # Need to show relatively new feeds.
    if request.method == "POST":
        comment = request.POST["comment"]
        post = user_models.ProfilePosts.objects.get(pk=request.POST["post_id"])
        models.Comments.objects.create(
            user=request.user, post=post, user_comment=comment
        )
    context = {"posts": posts}
    return render(request, "community/globalFeed.html", context=context)


@login_required(login_url="sign-in")
def updateLikeCount(request, pk, like):
    post = user_models.ProfilePosts.objects.get(pk=pk)
    if like == "yes":
        post.like_count += 1
        user_models.PostLikedData.objects.create(post=post, profile=request.user)
    elif like == "no":
        if post.like_count != 0:
            post.like_count -= 1
            temp = user_models.PostLikedData.objects.get(
                post=post, profile=request.user
            )
            temp.delete()
    post.save()

    return redirect("global-feed")
