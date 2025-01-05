from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required 
from rest_framework import viewsets

from django.conf import settings # new
from django.contrib.auth import logout # new
import urllib.parse # new

from main.utils import load_citizens_from_api
from main.models import Citizen, TaxpayerProfile
from main.serializers import TaxpayerProfileSerializer




class TaxpayerProfileViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows tax payer profiles to be viewed or edited.
  """
  queryset = TaxpayerProfile.objects.all()
  serializer_class = TaxpayerProfileSerializer

@login_required 
def home(request):
   citizens = Citizen.objects.all()
   return render(request, 'home.html', {'citizens': citizens})


def load_citizens_view(request):
   load_citizens_from_api()
   return redirect('home')


# new
def keycloak_logout(request):
    # Log out the user in Django
    logout(request)
    
    # Keycloak logout endpoint
    keycloak_logout_url = (
        f"http://localhost:8080/realms/demo/protocol/openid-connect/logout"
        f"?redirect_uri={urllib.parse.quote(settings.LOGOUT_REDIRECT_URL)}"
    )

    # Redirect to Keycloak logout
    return redirect(keycloak_logout_url)
