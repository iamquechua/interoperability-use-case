from django.contrib import admin
from django.urls import path


from main.views import home, load_citizens_view # new


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', home, name='home'), # new
   path('load_citizens/', load_citizens_view, name='load_citizens'), # new
]