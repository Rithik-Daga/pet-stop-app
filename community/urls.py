from . import views
from django.urls import path

urlpatterns = [
    path("global-feed/", views.globalFeed, name="global-feed"),
    path(
        "update-like/<uuid:pk>/<str:like>/",
        views.updateLikeCount,
        name="update-like-count",
    ),
]
