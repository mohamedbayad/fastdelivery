from django.db import models
from django.contrib.auth.models import User
from packages.models import *


# Create your models here.


class ProfileManDelivery(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    
    DisplayFields = ["id", "user", "first_name", "last_name", "city", "phone_number"]
    SearchbleFields = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class ProfileAdminDelivery(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    packages = models.ManyToManyField(NewPackage, blank=True)
    men_delivery = models.ManyToManyField(ProfileManDelivery, blank=True)
    
    DisplayFields = ["id", "user", "phone_number", "city"]
    SearchbleFields = ['phone_number', 'city']
    
    def __str__(self):
        return str(self.user)


class AddPackage(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    man_delivery = models.ForeignKey(
        ProfileManDelivery, on_delete=models.CASCADE, blank=True, null=True)
    set_packages = models.ManyToManyField(NewPackage, blank=True)

    DisplayFields = ["id", "user", "man_delivery"]

    def __str__(self):
        return f"package {self.man_delivery}"
