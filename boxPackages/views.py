from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewBox
from dashboard.models import *
from .forms import *
import uuid
from account.decorators import *


# Create your views here.

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def showBoxPackages(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    show_box = NewBox.objects.filter(user=request.user)
    context = {
        "show_box":show_box,
        "settings":settings,
        "profileImage":profileImage,
    }
    return render(request, "dashbord/pages/box-packages/box_packages.html", context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def addNewBox(request):
    id_box = uuid.uuid4()
    new_box = AddNewBox()
    try:
        if request.method == "POST":
            new_box = AddNewBox(request.POST)
            if new_box.is_valid():
                obj = new_box.save(commit=False)
                obj.user = request.user
                obj.id_box = id_box.hex[0:15]
                obj.save()
                messages.success(request, "Le box a été ajoutée avec succès")
                return redirect("add_new_box")
    except:
        return redirect("box_packages")

    return render(request, "dashbord/pages/box-packages/add_box.html")


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def deleteBox(request, pk):
    delete_box = NewBox.objects.get(user=request.user, id_box=pk)
    delete_box.delete()
    return redirect("box_packages")


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def pdfBox(request, pk):
    profile = Profile.objects.get(user=request.user)
    show_box = NewBox.objects.filter(user=request.user, id_box=pk)
    context = {
        "show_box":show_box,
        "profile":profile,
    }
    return render(request, "dashbord/pdf/box.html", context)