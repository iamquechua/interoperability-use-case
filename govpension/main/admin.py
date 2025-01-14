from django.contrib import admin
from .models import Citizen, RetireeProfile, TaxpayerProfile


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
   pass


@admin.register(RetireeProfile)
class RetireeProfileAdmin(admin.ModelAdmin):
   pass


@admin.register(TaxpayerProfile)
class TaxpayerProfileAdmin(admin.ModelAdmin):
   pass