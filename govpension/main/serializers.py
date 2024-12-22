from rest_framework import serializers
from .models import RetireeProfile




class RetireeProfileSerializer(serializers.ModelSerializer):
    citizen_number = serializers.SerializerMethodField()
    total_tax_contribution = serializers.SerializerMethodField()
    class Meta:
       model = RetireeProfile
       fields = ['id', 'citizen_number', 'total_tax_contribution', 'yearly_pension_allowance']


    def get_citizen_number(self, obj):
        return obj.citizen.citizen_number
    
    def get_total_tax_contribution(self, obj):
        return obj.citizen.taxpayer_profile.total_tax_contribution