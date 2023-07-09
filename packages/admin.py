from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(NewPackage)
class NewPackageAdmin(admin.ModelAdmin):
    list_display = NewPackage.DisplayFields
    search_fields = NewPackage.SearchbleFields

@admin.register(RefundRequest)
class RefundRequestAdmin(admin.ModelAdmin):
    list_display = RefundRequest.DisplayFields
    search_fields = RefundRequest.SearchbleFields

@admin.register(ExchangeRequest)
class ExchangeRequestAdmin(admin.ModelAdmin):
    list_display = ExchangeRequest.DisplayFields
    search_fields = ExchangeRequest.SearchbleFields