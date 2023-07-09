from django.shortcuts import render, redirect
from account.decorators import *
from .models import City

# Create your views here.

@loggedUser
def home(request):
    citys = City.objects.all()
    context = {
        "citys" : citys[:8]
    }
    return render(request, "base/home.html", context)

@loggedUser
def allCitys(request):
    citys = City.objects.all()
    context = {
        "citys" : citys
    }
    return render(request, 'base/pages/all_city.html', context)