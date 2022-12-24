from django.shortcuts import render, redirect
from .models import City

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else :
        citys = City.objects.all()
        context = {
            "citys" : citys
        }
        return render(request, "main\\home.html", context)