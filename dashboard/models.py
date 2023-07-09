from django.db import models
from django import forms
from django.contrib.auth.models import User
from main.models import *
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    TYPEBANK = (
        ("CIH", "CIH"),
        ("Al Barid Bank", "Al Barid Bank"),
        ("Attijariwafa Bank", "Attijariwafa Bank"),
        ("BMCE", "BMCE"),
        ("Société générale", "Société générale"),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, )
    address = models.CharField(max_length=100)
    bank = models.CharField(max_length=50, choices=TYPEBANK)
    rip = models.CharField(max_length=27)
    total_money_net = models.IntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to="profiles/%Y/%m/%d", null=True, blank=True)

    DisplayFields = ["id", "first_name", "last_name", "business_name", "phone", "address", "bank", "rip", "total_money_net"]
    SearchbleFields = ["first_name", "last_name", "business_name", "phone"]

    def __str__(self):
        return self.first_name

class Setting(models.Model):
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    DisplayFields = ["id", "title", "topic", "date"]
    SearchbleFields = ["title", "topic", "date"]

    def __str__(self):
        return self.title