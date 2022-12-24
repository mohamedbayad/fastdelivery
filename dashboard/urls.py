from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("editer-le-profil/<int:pk>", views.updateProfile, name="update-profile"),
]