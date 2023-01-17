from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class NewBox(models.Model):
    TYPE = [
        ("Liquide", "Liquide"),
        ("Solide", "Solide"),
    ]
    ETAT = [
        ("En coure ...", "En coure ..."),
        ("Valider", "Valider"),
    ]
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    id_box = models.CharField(max_length=100, null=True, blank=True)
    number_packages = models.CharField(max_length=50, null=True, blank=True)
    type_box = models.CharField(max_length=100, null=True, blank=True, choices=TYPE)
    etat = models.CharField(max_length=100, null=True, blank=True, default=ETAT[0][0], choices=ETAT)
    date = models.CharField(max_length=100, blank=True, null=True, default=timezone.now().strftime('%d-%m-%Y'))

    def __str__(self) -> str:
        return self.id_box