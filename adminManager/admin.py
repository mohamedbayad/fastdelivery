from django.contrib import admin
from .models import *

# Register your models here.


# admin.site.register(ProfileManDelivery)
# admin.site.register(ProfileAdminDelivery)
# admin.site.register(AddPackage)

@admin.register(ProfileManDelivery)
class ProfileManDeliveryAdmin(admin.ModelAdmin):
    list_display = ProfileManDelivery.DisplayFields
    search_fields = ProfileManDelivery.SearchbleFields

    

@admin.register(ProfileAdminDelivery)
class ProfileAdminDeliveryAdmin(admin.ModelAdmin):
    list_display = ProfileAdminDelivery.DisplayFields
    search_fields = ProfileAdminDelivery.SearchbleFields
    

@admin.register(AddPackage)
class AddPackageAdmin(admin.ModelAdmin):
    list_display = AddPackage.DisplayFields
    

