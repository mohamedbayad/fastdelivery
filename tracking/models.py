from django.db import models
from pickup.models import *
from django.contrib.auth.models import User

# Create your models here.

class Tracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    received = models.ForeignKey(Received, on_delete=models.CASCADE, null=True, blank=True)
    id_received = models.CharField(max_length=200, null=True, blank=True)
    tracking_number = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    warehouse = models.BooleanField(default=False, null=True, blank=True)
    city = models.BooleanField(default=False, blank=True, null=True)
    livry = models.BooleanField(default=False, blank=True, null=True)

    DisplayFields = ["id", "id_received", "user", "received", "tracking_number", "date"]
    SearchbleFields = ["id_received", "tracking_number"]

    def __str__(self) -> str:
        return self.tracking_number