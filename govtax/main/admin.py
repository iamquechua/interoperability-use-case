from django.contrib import admin
from .models import Citizen, TaxpayerProfile




@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
  pass


@admin.register(TaxpayerProfile)
class TaxpayerProfileAdmin(admin.ModelAdmin):
  list_display = ('citizen', 'total_tax_contribution',) # new