from django.core.management.base import BaseCommand
from inventory.models import Product, InventoryTransaction


class Command(BaseCommand):
    help = 'Populates the database with example products and inventory transactions'

    def handle(self, *args, **kwargs):
        # Create example products
        products = [
            {'name': 'Handmade Mug', 'description': 'A beautiful handmade mug.', 'price': 15.00, 'stock': 50},
            {'name': 'Apple', 'description': 'A very healthy fruit.', 'price': 3.00, 'stock': 20},
            {'name': 'Art Paint Set', 'description': 'A set of vibrant colors.', 'price': 25.00, 'stock': 30},
            {'name': 'Craft Paper Pack', 'description': 'A pack of high-quality craft paper.', 'price': 10.00, 'stock': 100},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

        # Create example inventory transactions
        transactions = [
            {'product': Product.objects.get(name='Handmade Mug'), 'transaction_type': 'RECEIVE', 'quantity': 20},
            {'product': Product.objects.get(name='Art Paint Set'), 'transaction_type': 'SELL', 'quantity': 5},
            {'product': Product.objects.get(name='Craft Paper Pack'), 'transaction_type': 'RECEIVE', 'quantity': 50},
        ]

        for transaction_data in transactions:
            transaction = InventoryTransaction.objects.create(**transaction_data)
            self.stdout.write(self.style.SUCCESS(f'Created transaction: {transaction}'))
