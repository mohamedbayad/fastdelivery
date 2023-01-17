from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from dashboard.models import *
from account.decorators import *

# Create your views here.


@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def dilevery_men(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile

    dilevery = Dilevery.objects.all()
    context = {
        "dilevery": dilevery,
        "settings": settings,
        "profileImage": profileImage,
    }
    return render(request, 'dashbord/pages/dilevery/dilevery.html', context)
