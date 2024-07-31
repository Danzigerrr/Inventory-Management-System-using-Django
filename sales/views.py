from django.shortcuts import render
from django.db.models import Sum, F
from inventory.models import Product, Purchase, InventoryTransaction
from django.contrib.auth.decorators import login_required
from users.models import Customer
from django.core.exceptions import PermissionDenied


# Helper function to check if user is admin
def is_admin(user):
    return user.is_superuser


@login_required
def sales_report(request):
    if not is_admin(request.user):
        raise PermissionDenied

    # Get all purchases with related product details
    purchases = Purchase.objects.select_related('product').annotate(
        total_price=F('quantity') * F('product__price')
    )

    # Calculate total sales
    total_sales = purchases.aggregate(total_sales=Sum('total_price'))['total_sales']

    # Calculate breakdown details
    breakdown = purchases.values(
        'product__name'
    ).annotate(
        total_quantity=Sum('quantity'),
        total_value=Sum('total_price')
    ).order_by('-total_value')

    # Get the most popular 10 products based on quantity sold
    popular_products = purchases.values(
        'product__name'
    ).annotate(
        total_quantity=Sum('quantity')
    ).order_by('-total_quantity')[:10]

    context = {
        'total_sales': format(total_sales, '.2f'),
        'breakdown': breakdown,
        'popular_products': popular_products,
    }

    return render(request, 'sales/sales_report.html', context)


@login_required
def inventory_report(request):
    if not is_admin(request.user):
        raise PermissionDenied

    transactions = InventoryTransaction.objects.all()
    inventory_levels = Product.objects.all()

    context = {
        'transactions': transactions,
        'inventory_levels': inventory_levels,
    }
    return render(request, 'sales/inventory_report.html', context)


@login_required
def customer_report(request):
    if not is_admin(request.user):
        raise PermissionDenied

    # Get all customers
    customers = Customer.objects.all()

    # Prepare a list to hold customer data along with their purchases
    customer_data = []
    for customer in customers:
        # Get all purchases related to this customer
        purchases = Purchase.objects.filter(user=customer.user)
        # Append a dictionary with customer and purchase details
        customer_data.append({
            'customer': customer,
            'purchases': purchases
        })

    context = {
        'customer_data': customer_data,
    }
    return render(request, 'sales/customer_report.html', context)

