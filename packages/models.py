from django.db import models
from django import forms
from boxPackages.models import NewBox
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy  as _

# Create your models here.

class NewPackage(models.Model):
    ETAT = [
        ("WAITING FOR PICKUP", _("WAITING FOR PICKUP")),
        ("In progress...", _("In progress...")),
        ("Exchange", _("Exchange")),
        ("Picked Up", _("Picked Up")),
        ("Cancelled", _("Cancelled")),
        ("Delivered", _("Delivered")),
        ("Refused", _("Refused")),
        ("No answer", _("No answer")),
        ("Returned/Cancelled", _("Returned/Cancelled")),
        ("Go back/Exchange", _("Go back/Exchange")),
        ("Returned/Refused", _("Returned/Refused")),
    ]
    id_package = models.CharField(max_length=100, null=True, blank=True)
    article_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    remark = models.TextField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.CharField(max_length=100, blank=True, null=True, default=timezone.now().strftime('%d-%m-%Y'))
    etat = models.CharField(max_length=100, default=ETAT[0][0], choices=ETAT, blank=True, null=True)
    picked_up = models.BooleanField(default=False, null=True, blank=True)
    withdrawn_canceled = models.IntegerField(default=0, null=True, blank=True)
    withdrawn_refused = models.IntegerField(default=0, null=True, blank=True)
    withdrawn_livery = models.IntegerField(default=0, null=True, blank=True)
    date_picked_up = models.CharField(max_length=100, blank=True, null=True, default=timezone.now().strftime('%d-%m-%Y'))
    exchange = models.BooleanField(default=False, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    box = models.ForeignKey(NewBox, on_delete=models.CASCADE, null=True, blank=True)

    DisplayFields = ["id_package", "article_name", "city", "client_name", "etat", "date_created", "picked_up"]
    SearchbleFields = ["id_package", "client_name", "date_created", "city"]

    def __str__(self):
        return f'{self.id_package}-{self.address}'


class RefundRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    refund_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    refund_price = models.IntegerField(null=True, blank=True, unique=True)
    refund = models.TextField(null=True, blank=False, unique=True)
    refund_date = models.DateTimeField(auto_now_add=True, unique=True)

    DisplayFields = ["id", "user", "refund_id", "refund_price", "refund", "refund_date"]
    SearchbleFields = ["refund_id"]

    def __str__(self):
        return self.refund


class ExchangeRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    exchange_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    exchange_price = models.IntegerField(null=True, blank=True, unique=True)
    exchange = models.TextField(null=True, blank=False, unique=True)
    exchange_date = models.DateTimeField(auto_now_add=True, unique=True)

    DisplayFields = ["id", "user", "exchange_id", "exchange_price", "exchange", "exchange_date"]
    SearchbleFields = ["exchange_id"]

    def __str__(self):
        return self.exchange
