from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = City.DisplayFields
    search_fields = City.SearchbleFields