from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from .forms import *
from main.models import *
from .models import *
from .filters import *
from dashboard.models import *
from account.decorators import *


# Create your views here.

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def newPackage(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile
    form = AddNewPackage()
    citys = City.objects.order_by("name")
    city = request.POST.get("city")
    id_pack = uuid.uuid1()
    if request.method == 'POST':
        City(name=city)
        form = AddNewPackage(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.id_package = id_pack.hex[0:11]
            if obj.city == 'Choisissez la ville':
                messages.error(request, 'Veuillez sélectionner une ville')
            elif not obj.phone_number.isnumeric():
                messages.error(request, 'Le numéro de téléphone ne peut pas contenir de lettres ou de symboles')
            else:
                obj.save()
                messages.success(request, 'colis ajouté avec succès')
                return redirect('new-packages')
    context = {
        "form": form,
        "citys": citys,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/package/add_new_package.html", context)

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def waitingPickup(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    packageData = NewPackage.objects.filter(user=request.user, picked_up=False)
    packageDataCount = packageData.count()
    context = {
        "packageData": packageData,
        "packageDataCount": packageDataCount,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/package/parcel_awaiting_pickup.html", context)

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def updatePackage(request, id):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    citys = City.objects.order_by("name")
    city = request.POST.get("city")
    order = NewPackage.objects.get(id_package=id)
    form = AddNewPackage(instance=order)
    if request.method == "POST":
        City(name=city)
        form = AddNewPackage(request.POST, instance=order)
        if form.is_valid():
            if order.city == 'Choisissez la ville':
                messages.error(request, 'Veuillez sélectionner une ville')
            elif not order.phone_number.isnumeric():
                messages.error(request, 'Le numéro de téléphone ne peut pas contenir de lettres ou de symboles')
            else:
                form.save()
                messages.success(request, 'Paquet changé avec succès')
                return redirect('packages-waiting-for-pickup')
    context = {
        'form': form,
        "citys": citys,
        "order": order,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/package/add_new_package.html", context)

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def deletPackage(request, id):
    order = NewPackage.objects.get(user=request.user, id_package=id)
    order.delete()
    messages.error(request, "Le paquet a été supprimé")
    return redirect("packages-waiting-for-pickup")

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def packagePickedUp(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    # ######### Get Data From DataBase ###########
    packageData = NewPackage.objects.filter(
        user=request.user).exclude(etat="EN ATTENTE DE RAMASSAGE")
    # packageData = NewPackages.objects.exclude(etat="EN ATTENTE DE RAMASSAGE")
    packageDataCount = NewPackage.objects.filter(user=request.user).exclude(
        etat="EN ATTENTE DE RAMASSAGE").count()
    # ######### form filter #########
    filterPackage = PackageFilter()
    if request.method == "GET":
        filterPackage = PackageFilter(request.GET, queryset=packageData)
        packageData = filterPackage.qs

    context = {
        "packageData": packageData,
        "packageDataCount": packageDataCount,
        "filterPackage": filterPackage,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/package/parcel_picked_up.html", context)

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def refundRequest(request, id):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    package = NewPackage.objects.filter(id_package=id)
    refund_count = RefundRequest.objects.filter(refund_id=id).count()
    price = package[0].price
    form = NewRefund()
    if request.method == "POST":
        form = NewRefund(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.refund_id = id
            obj.user = request.user
            obj.refund_price = package[0].price
            obj.save()
            messages.success(request, "Le retour a été demandé avec succès")
            return redirect("packages-pickup")
    contextform = {
        "refund_count": refund_count,
        "price": price,
        "form": form,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/parts-tool/refund.html", contextform)

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def exchangeRequest(request, id):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    package = NewPackage.objects.filter(id_package=id)
    exchange_count = ExchangeRequest.objects.filter(exchange_id=id).count()
    price = package[0].price
    form = NewExchange()
    if request.method == "POST":
        form = NewExchange(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.exchange_id = id
            obj.user = request.user
            obj.exchange_price = package[0].price
            obj.save()
            messages.success(request, "Demande de décaissement complétée avec succès")
            return redirect("packages-pickup")
    contextform = {
        "exchange_count": exchange_count,
        "price": price,
        "form": form,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/parts-tool/exchange.html", contextform)

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def parcelTracking(request):
    return render(request, "dashbord/pages/package/parcel_tracking.html")

@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def staticColis(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    # ############# data #############
    count_pick_up = NewPackage.objects.filter(
        user=request.user, etat="Ramassée").count()
    count_cancelled = NewPackage.objects.filter(
        user=request.user, etat="Annulée").count()
    count_livery = NewPackage.objects.filter(
        user=request.user, etat="Livrée").count()
    count_no_answer = NewPackage.objects.filter(
        user=request.user, etat="Pas de réponse").count()
    count_returned_cancelled = NewPackage.objects.filter(
        user=request.user, etat="Retournée/Annulée").count()
    context = {
        "data": {
            "count_pick_up": count_pick_up,
            "count_cancelled": count_cancelled,
            "count_livery": count_livery,
            "count_no_answer": count_no_answer,
            "count_returned_cancelled": count_returned_cancelled,
        },
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/package/parcel_statistics.html", context)
