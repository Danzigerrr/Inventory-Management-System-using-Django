from django.contrib import admin
from .models import Product, InventoryTransaction, Purchase

admin.site.register(Product)
admin.site.register(InventoryTransaction)
admin.site.register(Purchase)
