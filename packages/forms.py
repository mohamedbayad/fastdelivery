from django.forms import ModelForm
from .models import *

class AddNewPackage(ModelForm):
    class Meta:
        model = NewPackage
        fields = "__all__"
        exclude = ['user', 'id_package']

class NewRefund(ModelForm):
    class Meta:
        model = RefundRequest
        fields = "__all__"
        exclude = ["package", "refund_date"]


class NewExchange(ModelForm):
    class Meta:
        model = ExchangeRequest
        fields = "__all__"
        exclude = ["package", "exchange_date"]