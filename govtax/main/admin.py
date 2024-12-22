from django.contrib import admin
from .models import Citizen, TaxPayerProfile


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
   pass

@admin.register(TaxPayerProfile)
class TaxPayerProfileAdmin(admin.ModelAdmin):
   pass