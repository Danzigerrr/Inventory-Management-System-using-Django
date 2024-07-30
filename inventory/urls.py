from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_inventory, name='manage_inventory'),
    path('add-product/', views.add_product, name='add_product'),
    path('search/', views.search_products, name='search_products'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('purchased/', views.purchased_products, name='purchased_products'),
]
