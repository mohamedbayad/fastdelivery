from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(NewBox)
class NewBoxAdmin(admin.ModelAdmin):
    list_display = NewBox.DisplayFields
    search_fields = NewBox.SearchbleFields
