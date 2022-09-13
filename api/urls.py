from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="get-routes"),
    path("users/", views.getUserData, name="get-users"),
    path("pets/", views.getPetData, name="get-pets"),
    path("posts/", views.GetPosts.as_view(), name="get-posts"),
]
