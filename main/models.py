from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    price_l = models.IntegerField()
    price_r = models.IntegerField()
    price_c = models.IntegerField()

    DisplayFields = ["id", "name", "price_l", "price_r", "price_c"]
    SearchbleFields = ["name"]

    def __str__(self):
        return self.name