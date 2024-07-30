from django.urls import path
from . import views

urlpatterns = [
    path('sales_report/', views.sales_report, name='sales_report'),
    path('inventory_report/', views.inventory_report, name='inventory_report'),
    path('customer_report/', views.customer_report, name='customer_report'),
]
