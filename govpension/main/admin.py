from django.contrib import admin
from .models import Retiree




@admin.register(Retiree)
class RetireeAdmin(admin.ModelAdmin):
   pass