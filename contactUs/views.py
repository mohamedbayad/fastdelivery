from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.decorators import *
from .models import *
from .forms import *
from dashboard.models import *

# Create your views here.

@login_required(login_url="login")
@admins_only
def contact_us(request):
    # data nav bar
    settings = Setting.objects.all()  # icon settings
    profileImage = Profile.objects.filter(user=request.user)  # icon profile
    formContact = ContactForms()
    if request.method == "POST":
        formContact = ContactForms(request.POST)
        if formContact.is_valid():
            obj = formContact.save()
            obj.user = User.objects.get(id=request.user.id)
            obj.save()
            return redirect("dashboard")
    context = {
        'settings':settings,
        'profileImage':profileImage,
    }
    return render(request, "dashbord/pages/contact_us.html", context)