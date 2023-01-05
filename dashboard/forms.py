from django.forms import ModelForm
from .models import *

class NewProfile(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
