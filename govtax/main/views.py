from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets # new

from main.utils import load_citizens_from_api
from main.models import Citizen, TaxpayerProfile # updated
from main.serializers import TaxpayerProfileSerializer # new



# new
class TaxpayerProfileViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows tax payer profiles to be viewed or edited.
  """
  queryset = TaxpayerProfile.objects.all()
  serializer_class = TaxpayerProfileSerializer


def home(request):
   citizens = Citizen.objects.all()
   return render(request, 'home.html', {'citizens': citizens})


def load_citizens_view(request):
   load_citizens_from_api()
   return redirect('home')