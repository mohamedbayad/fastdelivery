from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class NewPackage(models.Model):
    ETAT = [
        ("EN ATTENTE DE RAMASSAGE", "EN ATTENTE DE RAMASSAGE"),
        ("Echange", "Echange"),
        ("Ramassée", "Ramassée"),
        ("Annulée", "Annulée"),
        ("Livrée", "Livrée"),
        ("Refusée", "Refusée"),
        ("Pas de réponse", "Pas de réponse"),
        ("Retournée/Annulée", "Retournée/Annulée"),
        ("Retoure/Echange", "Retoure/Echange"),
        ("Retournée/Refusée", "Retournée/Refusée"),
    ]
    id_package = models.CharField(max_length=100, null=True, blank=True)
    article_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    remark = models.TextField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.CharField(max_length=100, blank=True, null=True, default=timezone.now().strftime('%d-%m-%Y'))
    etat = models.CharField(max_length=100, default=ETAT[0][0], choices=ETAT, null=True, blank=True)
    picked_up = models.BooleanField(default=False, null=True, blank=True)
    withdrawn_canceled = models.IntegerField(default=0, null=True, blank=True)
    withdrawn_refused = models.IntegerField(default=0, null=True, blank=True)
    withdrawn_livery = models.IntegerField(default=0, null=True, blank=True)
    date_picked_up = models.CharField(max_length=100, blank=True, null=True, default=timezone.now().strftime('%d-%m-%Y'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id_package}-{self.address}'


class RefundRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    refund_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    refund_price = models.CharField(max_length=100, null=True, blank=True, unique=True)
    refund = models.TextField(null=True, blank=False, unique=True)
    refund_date = models.DateTimeField(auto_now_add=True, unique=True)

    def __str__(self):
        return self.refund


class ExchangeRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    exchange_id = models.CharField(max_length=100, null=True, blank=True)
    exchange_price = models.CharField(max_length=100, null=True, blank=True)
    exchange = models.TextField(null=True, blank=False)
    exchange_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exchange
