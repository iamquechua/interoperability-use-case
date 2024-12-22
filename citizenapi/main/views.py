from rest_framework import viewsets
from .models import Citizen
from .serializers import CitizenSerializer


class CitizenViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows citizens to be viewed or edited.
   """
   queryset = Citizen.objects.all()
   serializer_class = CitizenSerializer