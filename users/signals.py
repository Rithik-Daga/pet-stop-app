from . import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


def createProfile(sender, instance, created, **kwargs):
    """
    This function is triggered whenever a user
    registers on the website and creats a profile
    for the user.
    """

    if created and not kwargs.get("raw", False):
        user = instance
        profile = models.UserProfile.objects.create(username=user.username, user=user)
    return


def deleteUser(sender, instance, **kwargs):
    """
    This function is used to delete the user data
    whenever the user deletes his/her profile.
    """
    user = instance.user
    user.delete()

    return


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=models.UserProfile)
