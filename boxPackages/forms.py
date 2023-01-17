from django.forms import ModelForm
from .models import *

class AddNewBox(ModelForm):
    class Meta:
        model = NewBox
        fields = "__all__"