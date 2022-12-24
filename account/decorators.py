from django.shortcuts import redirect
from django.http import HttpResponse


def loggedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            groupe = None
            if request.user.groups.exists():
                groupe = request.user.groups.all()[0].name
            if groupe in allowedGroups:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("This page is not available to you")
        return wrapper_func
    return decorator


from adminManager.models import *

def admins_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        groupe = None
        if request.user.groups.exists():
            groupe = request.user.groups.all()[0].name
        if groupe == "customer":
            return view_func(request, *args, **kwargs)
        if groupe == "admin":
            return redirect("dashboard-admin")
        if groupe == "admins-delivery":
            return redirect("view_admin", request.user.id)
        if groupe == "delivery":
            return redirect("view_delivery", request.user.id)

    return wrapper_func
