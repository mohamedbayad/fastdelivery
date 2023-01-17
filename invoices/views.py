from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pickup.models import Received
from main.models import *
from packages.models import *
from dashboard.models import *
from account.decorators import *

# Create your views here.


def calc(parcel_inv):
    citys = City.objects.all()
    price = 0
    withdraw = 0
    t_w = 0
    packages = ""
    for parcel in parcel_inv:
        packages = parcel.packages.all()
        for pack in packages:
            if "Annulée" in pack.etat:
                for city in citys:
                    if city.name == pack.city:
                        withdraw = city.price_c
                        break
                pack.withdrawn_canceled = withdraw
            if "Refusée" in pack.etat:
                for city in citys:
                    if city.name == pack.city:
                        withdraw = city.price_r
                        break
                pack.withdrawn_refused = withdraw
            if "Livrée" in pack.etat:
                price += pack.price
                for city in citys:
                    if city.name == pack.city:
                        withdraw = city.price_l
                        break
                pack.withdrawn_livery = withdraw
            t_w += int(pack.withdrawn_canceled +
                        pack.withdrawn_refused + pack.withdrawn_livery)
            pack.save()
        parcel.total_withdrawn = t_w
        parcel.total_amount = price - parcel.total_withdrawn
        parcel.save()
        price = 0
        withdraw = 0
        t_w = 0
    

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def parcel_not_inv(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    parcel_inv = Received.objects.filter(user=request.user, invoise=False)
    parcel_invCount = Received.objects.filter(
        user=request.user, invoise=False, receive=True).count()
    
    calc(parcel_inv)

    context = {
        "parcel_inv": parcel_inv,
        "parcel_invCount": parcel_invCount,
        # "packages": packages,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/invoices/parcel_not_invoiced.html", context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def parcel_inv(request):
    # data nav top
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    parcel_inv = Received.objects.filter(user=request.user, invoise=True)
    parcel_invCount = Received.objects.filter(
        user=request.user, invoise=True, receive=True).count()
    
    calc(parcel_inv)

    context = {
        "parcel_inv": parcel_inv,
        "parcel_invCount": parcel_invCount,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, "dashbord/pages/invoices/parcel_invoiced.html", context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def parcel_inv_packages(request, id):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    parcel_inv_packs = Received.objects.filter(
        user=request.user, received_id=id)
    count_packages = 0
    for inv in parcel_inv_packs:
        count_packages = inv.packages.all().count()
    context = {
        "parcel_inv_packs": parcel_inv_packs,
        "count_packages": count_packages,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, 'dashbord/pages/invoices/parts-inv/packages.html', context)


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def pdfInvoices(request, pk):
    
    profile = Profile.objects.get(user=request.user)

    dataPackages = Received.objects.filter(
        user=request.user, received_id=pk)
    
    total_price = 0
    total_withdraw = 0
    
    for package in dataPackages:
        for t in package.packages.all():
            if t.etat == "Livrée":
                total_price += t.price
        total_withdraw += package.total_withdrawn

    context = {
        "dataPackages": dataPackages,
        "total_price": total_price,
        "total_withdraw": total_withdraw,
        "profile": profile,
    }
    return render(request, "dashbord/pdf/invoices.html", context)













    # citys = City.objects.all()
    # price = 0
    # withdraw = 0
    # t_w = 0
    # packages = ""
    # for parcel in parcel_inv:
    #     packages = parcel.packages.all()
    #     for pack in packages:
    #         if "Annulée" in pack.etat:
    #             for city in citys:
    #                 if city.name == pack.city:
    #                     withdraw = city.price_c
    #                     break
    #             pack.withdrawn_canceled = withdraw
    #         if "Refusée" in pack.etat:
    #             for city in citys:
    #                 if city.name == pack.city:
    #                     withdraw = city.price_r
    #                     break
    #             pack.withdrawn_refused = withdraw
    #         if "Livrée" in pack.etat:
    #             price += pack.price
    #             for city in citys:
    #                 if city.name == pack.city:
    #                     withdraw = city.price_l
    #                     break
    #             pack.withdrawn_livery = withdraw
    #         t_w += int(pack.withdrawn_canceled +
    #                     pack.withdrawn_refused + pack.withdrawn_livery)
    #         pack.save()
    #     parcel.total_withdrawn = t_w
    #     parcel.total_amount = price - parcel.total_withdrawn
    #     parcel.save()
    #     price = 0
    #     withdraw = 0
    #     t_w = 0
    