from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, InventoryTransaction, Purchase
from .forms import InventoryTransactionForm, ProductForm, ProductSearchForm, PurchaseForm
from django.contrib.auth.decorators import login_required


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


def search_products(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()
    if form.is_valid():
        query = form.cleaned_data['query']
        products = products.filter(name__icontains=query)
    return render(request, 'inventory/search_products.html', {'form': form, 'products': products})

@login_required
def buy_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.product = product
            if product.stock >= purchase.quantity:
                product.stock -= purchase.quantity
                product.save()
                purchase.save()
                messages.success(request, 'Purchase successful.')
                return redirect('profile')
            else:
                messages.error(request, 'Not enough stock available.')
    else:
        form = PurchaseForm(initial={'product': product})
    return render(request, 'inventory/buy_product.html', {'form': form, 'product': product})

@login_required
def purchased_products(request):
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'inventory/purchased_products.html', {'purchases': purchases})
