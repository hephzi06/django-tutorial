from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('baseapp.urls')),
    path('api/', include('baseapp.api.urls'))
]
