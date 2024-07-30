from django import forms
from .models import Product, InventoryTransaction, Purchase


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']


class InventoryTransactionForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        fields = ['product', 'transaction_type', 'quantity']


class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search Products', max_length=255)


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'quantity']
