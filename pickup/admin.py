from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Received)
class ReceivedAdmin(admin.ModelAdmin):
    list_display = Received.DisplayFields
    search_fields = Received.SearchbleFields