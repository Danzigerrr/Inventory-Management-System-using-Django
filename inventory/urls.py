from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_inventory, name='manage_inventory'),
    path('add-product/', views.add_product, name='add_product'),
]
