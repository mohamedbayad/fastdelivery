from django.urls import path
from . import views

urlpatterns = [
    path("", views.dilevery_men, name="dilevery_men"),
]