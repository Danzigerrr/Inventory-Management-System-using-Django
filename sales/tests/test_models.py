from django.test import TestCase
from inventory.models import Product
from .utils import create_sample_data
from sales.models import Sale


class SaleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        create_sample_data()

    def test_sale_creation(self):
        sale = Sale.objects.create(product=Product.objects.get(name='Product1'), quantity=2)
        self.assertEqual(sale.quantity, 2)
        self.assertEqual(sale.product.name, 'Product1')

    def test_sale_stock_reduction(self):
        product = Product.objects.get(name='Product1')
        initial_stock = product.stock
        Sale.objects.create(product=product, quantity=2)
        product.refresh_from_db()  # Refresh the product from the database to get the updated stock
        self.assertEqual(product.stock, initial_stock - 2)

    def test_sale_total_amount(self):
        product = Product.objects.get(name='Product1')
        sale = Sale.objects.create(product=product, quantity=2)
        expected_total_amount = sale.quantity * sale.product.price
        self.assertEqual(expected_total_amount, product.price * 2)
