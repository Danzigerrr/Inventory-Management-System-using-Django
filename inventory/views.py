from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, InventoryTransaction
from .forms import InventoryTransactionForm, ProductForm


def manage_inventory(request):
    if request.method == 'POST':
        form = InventoryTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            product = transaction.product
            if transaction.transaction_type == 'RECEIVE':
                product.stock += transaction.quantity
            elif transaction.transaction_type == 'SELL':
                if product.stock >= transaction.quantity:
                    product.stock -= transaction.quantity
                else:
                    messages.error(request, 'Not enough stock to complete this transaction.')
                    return redirect('manage_inventory')
            product.save()
            transaction.save()
            messages.success(request, 'Transaction completed successfully.')
            return redirect('manage_inventory')
    else:
        form = InventoryTransactionForm()
    products = Product.objects.all()
    transactions = InventoryTransaction.objects.all().order_by('-date')
    return render(request, 'inventory/manage_inventory.html', {
        'form': form,
        'products': products,
        'transactions': transactions,
    })


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})
