from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(NewPackage)
admin.site.register(RefundRequest)
admin.site.register(ExchangeRequest)