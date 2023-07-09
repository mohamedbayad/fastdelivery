from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = Tracking.DisplayFields
    search_fields = Tracking.SearchbleFields