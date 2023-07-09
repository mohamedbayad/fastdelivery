from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.decorators import *
from dashboard.models import *
from .models import *
from .filters import *

# Create your views here.

@login_required(login_url="connexion")
@allowedUsers(allowedGroups=["customer"])
def tracking(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile


    trackingData = None
    formTrackingNumber = TrackingFilter()
    if request.method == "GET":
        trackingData = Tracking.objects.filter(user=request.user)
        formTrackingNumber = TrackingFilter(request.GET, queryset=trackingData)
        trackingData = formTrackingNumber.qs
    
    context = {
        "trackingData":trackingData,
        "formTrackingNumber":formTrackingNumber,
        "settings":settings,
        "profileImage":profileImage,
    }
    return render(request, "dashboard/pages/tracking.html", context)