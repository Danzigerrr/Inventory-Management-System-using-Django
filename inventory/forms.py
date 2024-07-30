from django import forms
from .models import Product, InventoryTransaction


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']


class InventoryTransactionForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        fields = ['product', 'transaction_type', 'quantity']
