from django.db import models
from packages.models import *
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Received(models.Model):
    received_id = models.CharField(max_length=100, default='None', null=True, blank=True)
    date_received = models.CharField(max_length=100, null=True, blank=True)
    packages = models.ManyToManyField(NewPackage, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    total_withdrawn = models.IntegerField(null=True, blank=True)
    receive = models.BooleanField(null=True, blank=True, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    invoise = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.received_id