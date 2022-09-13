from email.policy import default
import uuid
from django.db import models
from utils.errors import PetProfileLimitError
from utils import helper_functions as hf
from django.contrib.auth.models import User

# Create your models here.
PET_PROFILE_LIMIT = 3


class UserProfile(models.Model):
    """
    Model class to store the user
    profile data.
    """

    id = models.UUIDField(
        verbose_name="Profile Id",
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    cover_image = models.ImageField(
        verbose_name="Cover Image",
        upload_to=hf.userDirectoryPath,
        null=True,
        blank=True,
    )
    profile_image = models.ImageField(
        verbose_name="Profile Image",
        upload_to=hf.userDirectoryPath,
        null=True,
        blank=True,
        default="/defaults/avatar.png",
    )
    bio = models.TextField(verbose_name="Bio", max_length=300, null=True)
    gender = models.CharField(max_length=10, verbose_name="Gender", null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class PetProfile(models.Model):
    """
    Model class to store the pet
    profile data.
    """

    id = models.UUIDField(
        verbose_name="Profile Id",
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    user_profile = models.ForeignKey(
        "UserProfile", on_delete=models.CASCADE, related_name="pets"
    )
    username = models.CharField(max_length=50, unique=True, verbose_name="Username")
    profile_image = models.ImageField(
        verbose_name="Profile Image",
        upload_to=hf.petDirectoryPath,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        pets = self.user_profile.pets.all()
        if len(pets) >= PET_PROFILE_LIMIT:
            raise PetProfileLimitError
        else:
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user_profile} --> {self.username}"


class ProfileFollowing(models.Model):
    user_id = models.ForeignKey(
        "UserProfile", on_delete=models.CASCADE, related_name="account"
    )
    follower_id = models.ForeignKey(
        "PetProfile", on_delete=models.CASCADE, related_name="follower"
    )

    def __str__(self):
        return f"{self.user_id} --> {self.follower_id}"


class ProfilePosts(models.Model):
    post_id = models.UUIDField(
        verbose_name="Post Id",
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    pet_profile = models.ForeignKey("PetProfile", on_delete=models.CASCADE)
    post = models.ImageField(upload_to=hf.postDirectoryPath, verbose_name="Post")
    caption = models.TextField(
        max_length=500, verbose_name="Caption", blank=True, null=True
    )
    like_count = models.IntegerField(verbose_name="Like Count", default=0)
    share_count = models.IntegerField(verbose_name="Share Count", default=0)
    unique_view_count = models.IntegerField(verbose_name="Unqiue View Count", default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    # time_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet_profile.username} -> {self.post_id}"


class PostLikedData(models.Model):
    profile = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="post_liked"
    )
    post = models.ForeignKey(
        "ProfilePosts", on_delete=models.CASCADE, related_name="liked_by"
    )
    liked = models.BooleanField(verbose_name="liked", default=False)
