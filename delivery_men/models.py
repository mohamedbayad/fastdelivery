from django.db import models

# Create your models here.

class Dilevery(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.username