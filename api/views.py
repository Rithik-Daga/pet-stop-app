from users import models
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def getRoutes(request):
    routes = {}
    return Response(routes)


@api_view(["GET"])
def getUserData(request):
    users = models.UserProfile.objects.all()
    serializer = serializers.UserProfileSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getPetData(request):
    pets = models.PetProfile.objects.all()
    serializer = serializers.PetProfileSerializer(pets, many=True)
    return Response(serializer.data)


class GetPosts(generics.ListAPIView):

    queryset = models.ProfilePosts.objects.all()
    serializer_class = serializers.ProfilePostSerializer

    def get_queryset(self):
        # Need to customize to get posts releated to users.
        return models.ProfilePosts.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
