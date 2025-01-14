from django.urls import include, path
from rest_framework import routers

from .views import CitizenViewSet


router = routers.DefaultRouter()
router.register(r'citizens', CitizenViewSet)


urlpatterns = [
   path('', include(router.urls)),
]
