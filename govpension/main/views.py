from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets # new


from main.utils import load_citizens_from_api, load_taxpayers_from_api, create_retiree_profiles
from main.models import Citizen, TaxpayerProfile, RetireeProfile # updated
from main.serializers import RetireeProfileSerializer




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


# new
class RetireeProfileViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows retiree profiles to be viewed or edited.
  """
  queryset = RetireeProfile.objects.all()
  serializer_class = RetireeProfileSerializer