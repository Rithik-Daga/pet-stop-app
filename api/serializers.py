from users import models
from rest_framework import serializers
from django.contrib.auth.models import User


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserDataSerializer()

    class Meta:
        model = models.UserProfile
        fields = "__all__"


class PetProfileSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer()

    class Meta:
        model = models.PetProfile
        fields = "__all__"


class ProfilePostSerializer(serializers.ModelSerializer):

    pet_profile = PetProfileSerializer()

    class Meta:
        model = models.ProfilePosts
        fields = "__all__"
