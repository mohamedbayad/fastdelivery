from django.forms import ModelForm
from .models import *

class FormReceived(ModelForm):
    class Meta:
        model = Received
        fields = "__all__"
        exclude = ['user']