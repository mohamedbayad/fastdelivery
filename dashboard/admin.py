from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = Profile.DisplayFields
    search_fields = Profile.SearchbleFields


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = Setting.DisplayFields
    search_fields = Setting.SearchbleFields
