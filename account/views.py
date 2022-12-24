from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import *
from .forms import *

# Create your views here.
@loggedUser
def register(request):
    form = CreateNewUser()
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès')
            return redirect("connexion")
    context = {
        "form" : form
    }
    return render(request, "base/pages/register.html", context)

@loggedUser
def userLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log = login(request, user)
            messages.success(request, 'Connexion réussie')
            return redirect("dashboard")
        else:
            messages.error(request, "Le mot de passe ou le nom de l'utilisateur est incorrect")
    return render(request, "base/pages/login.html")

def userLogout(request):
    logout(request)
    return redirect("connexion")

