from rest_framework import serializers
from .models import TaxpayerProfile




class TaxpayerProfileSerializer(serializers.ModelSerializer):


   citizen_number = serializers.SerializerMethodField()

   class Meta:
       model = TaxpayerProfile
       fields = ['id', 'citizen_number', 'total_tax_contribution']

   def get_citizen_number(self, obj):
       return obj.citizen.citizen_number