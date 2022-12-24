from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import *
from .models import *
from packages.models import *
from pickup.models import *
from main.models import *
from .statistics import countCitys
import datetime
from account.decorators import *
# Create your views here.


@login_required(login_url="login")
@admins_only
def dashboard(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    # data statistics
    packages = NewPackage.objects.filter(user=request.user)
    listCityPack = []
    listDatePack = []
    for pack in packages:
        listCityPack.append(pack.city)
        listDatePack.append(pack.date_created)

    # data statistics withe city
    listCity = []
    listCityCount = []
    for p in listCityPack:
        result = countCitys(listCityPack, p)
        if p not in listCity:
            listCity.append(p)
            listCityCount.append(result)

    # data statistics withe days
    listDays = []
    listDaysCount = []
    for d in listDatePack:
        result = countCitys(listDatePack, d)
        if d not in listDays:
            listDays.append(d)
            listDaysCount.append(result)
    

    package_no_invoices = Received.objects.filter(
        user=request.user, invoise=False)
    package_invoices = Received.objects.filter(user=request.user, invoise=True)

    packages_return = NewPackage.objects.filter(
        user=request.user)
    pack_list_returned = []
    for p_r in packages_return:
        if p_r.etat == "Retournée/Annulée" or p_r.etat == "Retoure/Echange" or p_r.etat == "Retournée/Refusée":
            pack_list_returned.append(p_r)

    TOTAL_NET_INCOME = 0
    for pack_inv in package_invoices:
        TOTAL_NET_INCOME += pack_inv.total_amount

    parcel_inv = Received.objects.filter(user=request.user, invoise=True)

    context = {
        "pack_list_returned": len(pack_list_returned),
        "package_no_invoices": package_no_invoices.count(),
        "package_invoices": package_invoices.count(),
        "TOTAL_NET_INCOME": TOTAL_NET_INCOME,
        "latest_packages": list(packages_return)[-10:],
        "parcel_inv": parcel_inv,
        "settings": settings,
        "profileImage": profileImage,
        "listCity":listCity,
        "listCityCount":listCityCount,
        "listDays":listDays,
        "listDaysCount":listDaysCount,
    }
    return render(request, "dashbord/dashbord.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def profile(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    form = NewProfile()
    if request.method == "POST":
        form = NewProfile(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(id=request.user.id)
            obj.save()
            return redirect("profile")
    data = {}
    info = Profile.objects.filter(user=request.user)
    for i in info:
        data = {
            'firstname': i.first_name,
            'lastname': i.last_name,
            'business_name': i.business_name,
            'phone': i.phone,
            'address': i.address,
            'bank': i.bank,
            'rip': i.rip,
        }

    context = {
        "form": form,
        "data": data,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/profile.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["customer"])
def updateProfile(request, pk):
    
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    _profile = Profile.objects.get(user=pk)
    form = NewProfile(instance=_profile)
    if request.method == "POST":
        form = NewProfile(request.POST, request.FILES, instance=_profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(id=request.user.id)
            obj.save()
            return redirect("profile")
    data = {}
    info = Profile.objects.filter(user=request.user)
    for i in info:
        data = {
            'firstname': i.first_name,
            'lastname': i.last_name,
            'business_name': i.business_name,
            'phone': i.phone,
            'address': i.address,
            'bank': i.bank,
            'rip': i.rip,
        }

    context = {
        "form": form,
        "data": data,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/update-profile.html", context)
