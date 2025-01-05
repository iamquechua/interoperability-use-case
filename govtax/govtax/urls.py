from django.urls import include, path
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

from main.views import home, keycloak_logout, load_citizens_view, TaxpayerProfileViewSet # updated


schema_view = get_schema_view(
 openapi.Info(
    title="GovTax API",
    default_version='v1',
    description="GovTax API",
    terms_of_service="https://www.sitename.com/policies/terms/",
    contact=openapi.Contact(email="contact@sitename.com"),
    license=openapi.License(name="BSD License"),
 ),
 public=True,
)


router = routers.DefaultRouter()
router.register(r'taxpayers', TaxpayerProfileViewSet)


urlpatterns = [
  path("admin/", admin.site.urls),
  path('oidc/', include('mozilla_django_oidc.urls')),
  path('', home, name='home'),
  path('logout/', keycloak_logout, name='logout'),  # new
  path('load_citizens/', load_citizens_view, name='load_citizens'),
  path('api/', include(router.urls)),
  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
