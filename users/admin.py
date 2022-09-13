from . import models
from django.contrib import admin


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "bio", "time_created", "time_updated"]
    list_editable = ["bio"]
    list_per_page = 50


class PetProfileAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "user_profile",
        "time_created",
        "time_updated",
        "is_active",
    ]
    list_editable = ["is_active"]
    list_per_page = 50


class ProfileFollowingAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "follower_id"]
    list_per_page = 50


class ProfilePostsAdmin(admin.ModelAdmin):
    list_display = [
        "post_id",
        "caption",
        "unique_view_count",
        "like_count",
        "share_count",
    ]
    list_per_page = 50


# Register your models here.
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.PetProfile, PetProfileAdmin)
admin.site.register(models.ProfileFollowing, ProfileFollowingAdmin)
admin.site.register(models.ProfilePosts, ProfilePostsAdmin)
admin.site.register(models.PostLikedData)
