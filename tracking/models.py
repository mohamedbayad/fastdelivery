from django.db import models
from packages.models import *

# Create your models here.

class Tracking(models.Model):
    package = models.ForeignKey(NewPackage, on_delete=models.CASCADE, blank=True, null=True)
    