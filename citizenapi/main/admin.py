from django.contrib import admin
from .models import Citizen


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
   pass