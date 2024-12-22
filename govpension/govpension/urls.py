from django.contrib import admin
from django.urls import path, include # updated
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new
from rest_framework import routers # new


from main.views import home, load_citizens_view, load_taxpayers_view, create_retiree_profiles_view, RetireeProfileViewSet # updated




# new
schema_view = get_schema_view(
 openapi.Info(
    title="Pension Management System API",
    default_version='v1',
    description="Pension Management System API",
    terms_of_service="https://www.sitename.com/policies/terms/",
    contact=openapi.Contact(email="contact@sitename.com"),
    license=openapi.License(name="BSD License"),
 ),
 public=True,
)


router = routers.DefaultRouter()
router.register(r'retirees', RetireeProfileViewSet)




urlpatterns = [
  path('admin/', admin.site.urls),
  path('', home, name='home'),
  path('load_citizens/', load_citizens_view, name='load_citizens'),
  path('load_taxpayers/', load_taxpayers_view, name='load_taxpayers'),
  path('create_retiree_profiles/', create_retiree_profiles_view, name='create_retiree_profiles'),
  path('api/', include(router.urls)), # new
  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), # new
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # new
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # new
]
