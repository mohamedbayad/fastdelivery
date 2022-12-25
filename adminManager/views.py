from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.decorators import *
from pickup.models import *
from packages.models import *
from dashboard.models import *
from packages.forms import *
from pickup.forms import *
from invoices.views import *
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your views here.


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin"])
def dashboardAdmin(request):
    # show all exchange
    exchanges = ExchangeRequest.objects.all()
    # show all refund
    refunds = RefundRequest.objects.all()
    # add packages to admin delivery
    appPackagesToAdminDelivery()
    # get all admins delivery
    admins_delivery = ProfileAdminDelivery.objects.all()
    # get all users
    users = Profile.objects.all()
    # get count packages
    total_packages = NewPackage.objects.all().count()
    # get count all packages delivered
    total_packages_deliveres = NewPackage.objects.filter(etat="Livrée").count()
    # get total fee by packages

    packages_fee = NewPackage.objects.all()
    
    TOTAL_FEE = 0
    
    # for pack in packages_fee:
    #     if pack.etat == "Annulée" or pack.etat == "Livrée" or pack.etat == "Refusée" or "Retournée" in pack.etat:
    #         TOTAL_FEE += pack.withdrawn_canceled + \
    #             pack.withdrawn_livery + pack.withdrawn_refused

    # get invoices
    package_invoices = Received.objects.filter(invoise=True)
    TOTAL_NET_INCOME = 0
    for pack_inv in package_invoices:
        TOTAL_NET_INCOME += pack_inv.total_amount
        TOTAL_FEE += pack_inv.total_withdrawn

    context = {
        "t_n_i_c": TOTAL_NET_INCOME,
        "t_p_d": total_packages_deliveres,
        "total_fee": TOTAL_FEE,
        "total_packages": total_packages,
        "users": users,
        "admins_delivery": admins_delivery,
        "exchanges": exchanges,
        "refunds": refunds,
    }

    return render(request, "dashboard-admin/dashboard.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin"])
def viewProfileUser(request, pk):

    # get data to send in cards
    total_packages_deliveres = NewPackage.objects.filter(
        user=pk, etat="Livrée").count()
    total_packages = NewPackage.objects.filter(user=pk).count()

    # packages = NewPackage.objects.filter(user=pk)
    packages = Received.objects.filter(user=pk, nvoise=True)

    TOTAL_FEE = 0
    TOTAL_NET_INCOME = 0
    FIN_TOTAL = 0

    for pack in packages:
        if pack.etat == "Annulée" or pack.etat == "Livrée" or pack.etat == "Refusée" or "Retournée" in pack.etat:
            TOTAL_FEE += pack.withdrawn_canceled + \
                pack.withdrawn_livery + pack.withdrawn_refused
            if pack.etat == "Livrée":
                TOTAL_NET_INCOME += pack.price

    FIN_TOTAL = TOTAL_NET_INCOME - TOTAL_FEE
    # --------------- end ---------------
    # get data invoices
    data_invoices = Received.objects.filter(user=pk)
    pdf_invoices = Received.objects.filter(user=pk, invoise=True)

    # get exchange and refund
    refunds = RefundRequest.objects.filter(user=pk)
    exchanges = ExchangeRequest.objects.filter(user=pk)

    calc(pdf_invoices)

    context = {
        "FIN_TOTAL": FIN_TOTAL,
        "TOTAL_FEE": TOTAL_FEE,
        "packages_count": total_packages,
        "total_packages_delivered": total_packages_deliveres,
        "data_invoices": data_invoices,
        "pdf_invoices": pdf_invoices,
        "packages": packages,
        "refunds": refunds,
        "exchanges": exchanges,
    }

    return render(request, "dashboard-admin/profile.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin"])
def veiwReceive(request, pk, npk):
    received_update = Received.objects.get(received_id=npk)
    formReceived = FormReceived(instance=received_update)
    if request.method == "POST":
        formReceived = FormReceived(request.POST, instance=received_update)
        if formReceived.is_valid():
            formReceived.save()
            return redirect("view_user", pk)
    context = {
        "formReceived": formReceived,
        "received_update": received_update,
    }

    return render(request, "dashboard-admin/received.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin"])
def pdfInvoicesAdmin(request, pk, npk):
    profile = Profile.objects.get(user=npk)

    dataPackages = Received.objects.filter(
        user=npk, received_id=pk)

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


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin", "admins-delivery", "delivery"])
def savePdfLb(request, pk, npk):
    dataPdf = Received.objects.filter(received_id=npk)
    profile = Profile.objects.get(user=dataPdf[0].user)
    context = {
        "dataPdf": dataPdf,
        "profile": profile,
    }
    return render(request, "dashbord/pdf/labels.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin", "admins-delivery", "delivery"])
def veiwPackages(request, pk, npk):
    obj = NewPackage.objects.get(user=pk, id_package=npk)
    formPackages = EditePackage(instance=obj)
    if request.method == "POST":
        formPackages = EditePackage(request.POST, instance=obj)
        if formPackages.is_valid():
            formPackages.save()
            return redirect('view_user', pk)
    context = {
        "formPackages": formPackages,
    }
    return render(request, 'dashboard-admin/packages.html', context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin"])
def viewRefund(request, pk, npk):

    refund_data = RefundRequest.objects.get(refund_id=npk)
    context = {
        "refund_data": refund_data
    }
    return render(request, 'dashboard-admin/refund.html', context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin"])
def viewExchange(request, pk, npk):
    exchange_data = ExchangeRequest.objects.get(exchange_id=npk)
    context = {
        "exchange_data": exchange_data
    }
    return render(request, 'dashboard-admin/exchange.html', context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin", "admins-delivery"])
def viewAdminMenDelivery(request, pk):
    # add packages to admin delivery
    appPackagesToAdminDelivery()

    data_admin = ProfileAdminDelivery.objects.filter(user=pk)

    TOTAL_MONEY = 0
    TOTAL_FEE = 0
    TOTAL_NET = 0
    TOTAL_PACKAGE_DELIVERED = 0
    packages = None
    total_packages = 0

    for item in data_admin:
        packages = item.packages.all()
        total_packages = packages.count()
        for package in packages:
            if package.etat == "Livrée":
                TOTAL_PACKAGE_DELIVERED += 1
                TOTAL_MONEY += package.price
                TOTAL_FEE += package.withdrawn_canceled + \
                    package.withdrawn_livery + package.withdrawn_refused
            else:
                TOTAL_FEE += package.withdrawn_canceled + \
                    package.withdrawn_livery + package.withdrawn_refused

    TOTAL_NET = TOTAL_MONEY - TOTAL_FEE

    MEN_DELIVERY = 0
    for delivery in data_admin:
        MEN_DELIVERY = delivery.men_delivery.count()

    context = {
        "data_admin": data_admin,
        "TOTAL_NET": TOTAL_NET,
        "total_packages": total_packages,
        "packages": packages,
        "MEN_DELIVERY": MEN_DELIVERY,
        "TOTAL_PACKAGE_DELIVERED": TOTAL_PACKAGE_DELIVERED,
    }
    return render(request, "dashboard-admin/admin_men_delivery.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin", "admins-delivery", "delivery"])
def viewManDelivery(request, pk):
    man_delivery = AddPackage.objects.filter(user=pk)

    TOTAL_MONEY = 0
    TOTAL_FEE = 0
    TOTAL_NET = 0
    TOTAL_PACKAGE_DELIVERED = 0

    for item in man_delivery:
        for price_pack in item.set_packages.all():
            if price_pack.etat == "Livrée":
                TOTAL_PACKAGE_DELIVERED += 1
                TOTAL_MONEY += price_pack.price
                TOTAL_FEE += price_pack.withdrawn_canceled + \
                    price_pack.withdrawn_livery + price_pack.withdrawn_refused
            else:
                TOTAL_FEE += price_pack.withdrawn_canceled + \
                    price_pack.withdrawn_livery + price_pack.withdrawn_refused

    TOTAL_NET = TOTAL_MONEY - TOTAL_FEE

    context = {
        "man_delivery": man_delivery,
        "TOTAL_NET": TOTAL_NET,
        "TOTAL_PACKAGE_DELIVERED": TOTAL_PACKAGE_DELIVERED,
    }
    return render(request, "dashboard-admin/profile_man_delivery.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin", "admins-delivery"])
def addPackages(request, pk):

    data_admin_delivery = ProfileAdminDelivery.objects.filter(user=pk)
    
    users_delivery = User.objects.filter(groups=4)

    packages_deli = AddPackage.objects.all()

    list_users_deli = []

    if request.method == "POST":

        user_deli = ProfileManDelivery.objects.get(
            id=request.POST.get("man_delivery")).user

        if packages_deli.count() == 0:
            formPackages = AddPackageToDelivery(request.POST)
        else:

            for pack in packages_deli:
                list_users_deli.append(pack.user)

            if user_deli in list_users_deli:
                pack_deli = AddPackage.objects.get(user=user_deli)
                formPackages = AddPackageToDelivery(
                    request.POST, instance=pack_deli)
            else:
                formPackages = AddPackageToDelivery(request.POST)

        if formPackages.is_valid():
            obj = formPackages.save()
            obj.user = user_deli
            obj.save()
            return redirect("add_packages", request.user.id)

    context = {
        # "formPackages": formPackages,
        "data_admin_delivery": data_admin_delivery,
        "users_delivery": users_delivery,
    }
    return render(request, "dashboard-admin/add_packages.html", context)


@login_required(login_url="login")
@allowedUsers(allowedGroups=["admin", "admins-delivery"])
def addManDelivery(request, pk):
    form_user = CreateNewUserDelivery()
    form_profile = CreateNewProfileDelivery()
    admin_deli = ProfileAdminDelivery.objects.get(user=request.user)
    if request.method == "POST":
        form_profile = CreateNewProfileDelivery(request.POST)
        form_user = CreateNewUserDelivery(request.POST)
        if form_user.is_valid():
            obj = form_user.save()
            group = Group.objects.get(name="delivery")
            obj.groups.add(group)
            obj.save()
            obj2 = form_profile.save(commit=False)
            obj2.user = User.objects.get(id=obj.id)
            obj2.save()
            admin_deli.men_delivery.add(obj2)
            return redirect("add_delivery", request.user.id)

    context = {
        # "form_user": form_user,
        # "form_profile": form_profile,
    }
    return render(request, "dashboard-admin/add_profile_delivery.html", context)


def appPackagesToAdminDelivery():
    packages = NewPackage.objects.all()
    admins_delivery = ProfileAdminDelivery.objects.all()
    for package in packages:
        for admin in admins_delivery:
            if package.city.lower() == admin.city.lower():
                admin.packages.add(package)
