from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("les-villes", views.allCitys, name="all_citys"),
]