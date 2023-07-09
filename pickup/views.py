from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dashboard.models import *
from packages.models import *
from packages.forms import *
from tracking.forms import AddNewTracking
from .models import *
from account.decorators import *
from django.contrib import messages
from django.utils import timezone
import uuid
from django.utils.translation import gettext as _


# Create your views here.

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def pickedup(request):
    formAddTracking = AddNewTracking() # add new tracking packages

    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    # ############# Get Data #############
    packagePickup = NewPackage.objects.filter(
        user=request.user, etat="WAITING FOR PICKUP", picked_up=False)
    id_received = uuid.uuid1()
    receiv = Received()
    m = ""
    # ############# Update Data #############
    count = 0
    try: 
        if request.method == "POST":
            id_package = request.POST.getlist("pickup-check")
            packages_picked_up = id_package
            receiv.received_id = id_received.hex[0:10]
            receiv.user = request.user
            receiv.total_withdrawn = 0
            receiv.total_amount = 0
            receiv.date_received = timezone.now().strftime('%d-%m-%Y')
            receiv.receive = False
            while True:
                picked_up = NewPackage.objects.get(id_package=id_package[count])
                picked_up_form = AddNewPackage(request.POST, instance=picked_up)
                picked_up.etat = "In progress..."
                picked_up.picked_up = True
                picked_up.date_picked_up = timezone.now().strftime('%d-%m-%Y')
                picked_up.save()
                receiv.save()
                receiv.packages.add(picked_up)
                count += 1
                if count == len(id_package):
                    objTracking = formAddTracking.save(commit=False)
                    objTracking.id_received = receiv.received_id
                    objTracking.tracking_number = uuid.uuid4()
                    objTracking.date = receiv.date_received
                    objTracking.received = receiv
                    objTracking.user = request.user
                    objTracking.save()
                    messages.success(request, _("Nouveau coupon créé avec succès"))
                    return redirect("pickup")
    except :
        messages.add_message(request, 50, _("Il n'y a pas d'élément à ajouter"))

    context = {
        "packagePickup": packagePickup,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/pages/pick_up/new_pick_up.html", context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def received(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    receiv = Received.objects.filter(user=request.user)
    receivCount = Received.objects.filter(
        user=request.user, receive=True).count()
    context = {
        "receiv": receiv,
        "receivCount": receivCount,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/pages/pick_up/pick_up_voucher_received.html", context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def no_received(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    noreceiv = Received.objects.filter(user=request.user)
    noreceivCount = Received.objects.filter(
        user=request.user, receive=False).count()
    context = {
        "noreceiv": noreceiv,
        "noreceivCount": noreceivCount,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/pages/pick_up/pickup_voucher_not_received.html", context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def no_received_del(request, id):
    receiv = Received.objects.filter(user=request.user, received_id=id)
    receivePackages = Received.objects.get(
        user=request.user, received_id=id).packages.all()
    for r in receivePackages:
        r.etat = "WAITING FOR PICKUP"
        r.picked_up = False
        r.save()
    receiv.delete()
    return redirect("collection-voucher-no-received")


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def savePdfLb(request, id):
    dataPdf = Received.objects.filter(received_id=id)
    profile = Profile.objects.get(user=request.user)
    context = {
        "dataPdf": dataPdf,
        "profile": profile,
    }
    return render(request, "dashboard/pdf/labels.html", context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def pdfPickeup(request, pk):
    profile = Profile.objects.get(user=request.user)
    dataPackages = Received.objects.filter(
        user=request.user, received_id=pk)
    total = 0
    for package in dataPackages:
        for t in package.packages.all():
            total += t.price
    context = {
        "dataPackages": dataPackages,
        "total": total,
        "profile": profile,
    }
    return render(request, "dashboard/pdf/pickedup.html", context)
