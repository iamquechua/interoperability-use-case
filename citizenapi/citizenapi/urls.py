from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new


# new
schema_view = get_schema_view(
 openapi.Info(
    title="Citizens API",
    default_version='v1',
    description="Citizens API",
    terms_of_service="https://www.sitename.com/policies/terms/",
    contact=openapi.Contact(email="contact@sitename.com"),
    license=openapi.License(name="BSD License"),
 ),
 public=True,
)

urlpatterns = [
  path("admin/", admin.site.urls),
  path("api/", include("main.urls")),
  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), # new
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # new
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # new
]
