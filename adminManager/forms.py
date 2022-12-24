from django.forms import ModelForm
from packages.models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewUserDelivery(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditePackage(ModelForm):
    class Meta:
        model = NewPackage
        fields = "__all__"
        exclude = ['user']


class AddPackageToDelivery(ModelForm):
    class Meta:
        model = AddPackage
        fields = "__all__"
        # exclude = ['id']


class CreateNewProfileDelivery(ModelForm):
    class Meta:
        model = ProfileManDelivery
        fields = "__all__"
        exclude = ["user"]
