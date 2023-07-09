from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from packages.models import *
from pickup.models import *
from main.models import *
from .statistics_1 import countCitys
from account.decorators import *
from django.contrib import messages
from django.utils.translation import gettext as _
from invoices.views import calc
# Create your views here.


@login_required(login_url="connexion")
@admins_only
def dashboard(request):

    parcel_inv = Received.objects.filter(user=request.user, invoise=True)
    
    # calc factur
    calc(parcel_inv)

    
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    # data statistics withe DATE
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

    # Total packages returned 
    packages_return = NewPackage.objects.filter(
        user=request.user)
    pack_list_returned = []
    for p_r in packages_return:
        if p_r.etat == "Returned/Cancelled" or p_r.etat == "Go back/Exchange" or p_r.etat == "Returned/Refused":
            pack_list_returned.append(p_r)

            
    TOTAL_NET_INCOME = 0
    try:
        # calc total net 
        profileMoney = Profile.objects.get(user=request.user)
        profileMoney.total_money_net = 0
        for pack_inv in package_invoices:
            profileMoney.total_money_net += pack_inv.total_amount
        
        TOTAL_NET_INCOME = profileMoney.total_money_net
        profileMoney.save()
    except:
        pass
    ############# end #############


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
    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="connexion")
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
    try:
        info = Profile.objects.get(user=request.user)
        data = {
            'firstname': info.first_name,
            'lastname': info.last_name,
            'business_name': info.business_name,
            'phone': info.phone,
            'address': info.address,
            'bank': info.bank,
            'rip': info.rip,
        }
    except:
        pass

    context = {
        "form": form,
        "data": data,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashboard/pages/profile.html", context)


@login_required(login_url="connexion")
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
    return render(request, "dashboard/pages/update-profile.html", context)
