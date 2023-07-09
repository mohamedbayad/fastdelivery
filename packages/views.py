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
from django.utils.translation import gettext as _


# Create your views here.
@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def newPackage(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile
    
    form = AddNewPackage()
    citys = City.objects.order_by("name")
    boxs = NewBox.objects.filter(etat="Validate", user=request.user)
    city = request.POST.get("city")
    id_pack = uuid.uuid1()
    if request.method == 'POST':
        
        City(name=city)
        form = AddNewPackage(request.POST)

        if form["city"].value() == 'Choisissez la ville':
            message = _("Veuillez sélectionner une ville")
            messages.error(request, message)
        elif not form["phone_number"].value().isnumeric():
            message = _("Le numéro de téléphone ne peut pas contenir de lettres ou de symboles")
            messages.error(request, message)
        elif form["box"].value() == "Choisissez la Boite":
            message = _("Avant de créer un package, vous devez d'abord créer la boîte de package")
            messages.error(request, message)
        
        if form.is_valid():
            print("Valid")
            obj = form.save(commit=False)
            obj.user = request.user
            obj.id_package = id_pack.hex[0:11]
            obj.save()
            message = _("colis ajouté avec succès")
            messages.success(request, message)
            return redirect('new-packages')
        

    context = {
        "form": form,
        "citys": citys,
        "settings": settings,
        "profileImage": profileImage,
        "boxs": boxs,
    }
    return render(request, "dashboard/pages/package/add_new_package.html", context)

@login_required(login_url="connexion")
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
    return render(request, "dashboard/pages/package/parcel_awaiting_pickup.html", context)

@login_required(login_url="connexion")
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
                messages.error(request, _('Veuillez sélectionner une ville'))
            elif not order.phone_number.isnumeric():
                messages.error(request, _('Le numéro de téléphone ne peut pas contenir de lettres ou de symboles'))
            else:
                form.save()
                messages.success(request, _('Paquet changé avec succès'))
                return redirect('packages-waiting-for-pickup')
    context = {
        'form': form,
        "citys": citys,
        "order": order,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/pages/package/add_new_package.html", context)

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def deletPackage(request, id):
    order = NewPackage.objects.get(user=request.user, id_package=id)
    order.delete()
    messages.error(request, _("Le paquet a été supprimé"))
    return redirect("packages-waiting-for-pickup")

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def packagePickedUp(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    # ######### Get Data From DataBase ###########
    packageData = NewPackage.objects.filter(
        user=request.user).exclude(etat="WAITING FOR PICKUP")
    # packageData = NewPackages.objects.exclude(etat="WAITING FOR PICKUP")
    packageDataCount = NewPackage.objects.filter(user=request.user).exclude(
        etat="WAITING FOR PICKUP").count()
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
    return render(request, "dashboard/pages/package/parcel_picked_up.html", context)

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def refundRequest(request, id):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    package = NewPackage.objects.get(id_package=id)

    refund_count = RefundRequest.objects.filter(refund_id=id).count()

    price = package.price
    form = NewRefund()
    if request.method == "POST":
        form = NewRefund(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.refund_id = id
            obj.user = request.user
            obj.refund_price = package.price
            obj.save()
            messages.success(request, _("Le retour a été demandé avec succès"))
            return redirect("packages-pickup")
    contextform = {
        "refund_count":refund_count,
        "price": price,
        "form": form,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/parts-tool/refund.html", contextform)

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def exchangeRequest(request, id):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    package = NewPackage.objects.get(id_package=id)

    exchange_count = ExchangeRequest.objects.filter(exchange_id=id).count()

    price = package.price
    form = NewExchange()
    if request.method == "POST":
        form = NewExchange(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.exchange_id = id
            obj.user = request.user
            obj.exchange_price = package.price
            obj.save()
            messages.success(request, _("Le retour a été demandé avec succès"))
            return redirect("packages-pickup")
    contextform = {
        "exchange_count": exchange_count,
        "price": price,
        "form": form,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/parts-tool/exchange.html", contextform)

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def change_address(request, id):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    citys = City.objects.order_by("name")
    orderPackage = NewPackage.objects.get(id_package=id)
    form = AddNewPackage(instance=orderPackage)
    if request.method == "POST":
        form = AddNewPackage(request.POST, instance=orderPackage)
        if form.is_valid():
            # form.save()
            obj = form.save(commit=False)
            obj.exchange = True
            obj.save()
            messages.success(request, _("Demande de décaissement complétée avec succès"))
            return redirect("packages-pickup")
    
    contextform = {
        "orderPackage": orderPackage,
        "citys": citys,
        "form": form,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/parts-tool/change-address.html", contextform)

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def staticColis(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    # ############# data #############
    count_pick_up = NewPackage.objects.filter(
        user=request.user, etat="Picked Up").count()
    count_cancelled = NewPackage.objects.filter(
        user=request.user, etat="Cancelled").count()
    count_livery = NewPackage.objects.filter(
        user=request.user, etat="Delivered").count()
    count_no_answer = NewPackage.objects.filter(
        user=request.user, etat="No answer").count()
    count_returned_cancelled = NewPackage.objects.filter(
        user=request.user, etat="Returned/Cancelled").count()
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
    return render(request, "dashboard/pages/package/parcel_statistics.html", context)
