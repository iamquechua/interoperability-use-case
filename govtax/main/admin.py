from django.contrib import admin
from .models import Taxpayer


@admin.register(Taxpayer)
class TaxpayerAdmin(admin.ModelAdmin):
   pass