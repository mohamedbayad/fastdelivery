from django.forms import ModelForm
from .models import *

class ContactForms(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ['user']