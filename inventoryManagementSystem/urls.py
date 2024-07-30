from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inventory/', include('inventory.urls')),
    # path('sales/', include('sales.urls')),
    # path('customers/', include('customers.urls')),
]
