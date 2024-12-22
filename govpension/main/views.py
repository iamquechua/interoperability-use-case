from django.shortcuts import render
from django.shortcuts import redirect
from main.utils import load_citizens_from_api
from main.models import Citizen



def home(request):
   citizens = Citizen.objects.all()
   return render(request, 'home.html', {'citizens': citizens})


def load_citizens_view(request):
   load_citizens_from_api()
   return redirect('home')