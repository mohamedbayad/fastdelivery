from django.forms import ModelForm
from .models import *

class AddNewTracking(ModelForm):
    class Meta:
        model = Tracking
        fields = "__all__"