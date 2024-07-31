from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('users/', include('users.urls')),
    path('sales/', include('sales.urls')),
    path('', RedirectView.as_view(url='/users/login/', permanent=False)),
]
