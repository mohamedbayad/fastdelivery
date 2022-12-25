from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.decorators import *
from .models import *
from .forms import *

# Create your views here.

@login_required(login_url="login")
@admins_only
def contact_us(request):
    formContact = ContactForms()
    if request.method == "POST":
        formContact = ContactForms(request.POST)
        if formContact.is_valid():
            formContact.save()
            return redirect("dashboard")
    return render(request, "dashbord/pages/contact_us.html")