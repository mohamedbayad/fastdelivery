from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user}-{self.email}"