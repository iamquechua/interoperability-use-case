from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required 
from rest_framework import viewsets

from django.conf import settings # new
from django.contrib.auth import logout # new
import urllib.parse # new


from main.utils import load_citizens_from_api, load_taxpayers_from_api, create_retiree_profiles
from main.models import Citizen, TaxpayerProfile, RetireeProfile 
from main.serializers import RetireeProfileSerializer


@login_required 
def home(request):
  citizens = Citizen.objects.all()
  taxpayers = TaxpayerProfile.objects.all
  return render(request, 'home.html', {'citizens': citizens, 'taxpayers': taxpayers})


def load_citizens_view(request):
  load_citizens_from_api()
  return redirect('home')


def load_taxpayers_view(request):
  load_taxpayers_from_api()
  return redirect('home')


def create_retiree_profiles_view(request):
  taxpayers = TaxpayerProfile.objects.all()
  create_retiree_profiles(taxpayers)
  return redirect('home')



class RetireeProfileViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows retiree profiles to be viewed or edited.
  """
  queryset = RetireeProfile.objects.all()
  serializer_class = RetireeProfileSerializer


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
