from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Product, InventoryTransaction, Purchase


class ProductModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Sample Product',
            description='A sample product description',
            price=10.99,
            stock=100
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Sample Product')


class InventoryTransactionModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Sample Product',
            price=10.99,
            stock=100
        )
        self.transaction = InventoryTransaction.objects.create(
            product=self.product,
            transaction_type='RECEIVE',
            quantity=10
        )

    def test_inventory_transaction_str(self):
        self.assertEqual(
            str(self.transaction),
            f"RECEIVE 10 of Sample Product"
        )


class PurchaseModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(
            name='Sample Product',
            price=10.99,
            stock=100
        )
        self.purchase = Purchase.objects.create(
            user=self.user,
            product=self.product,
            quantity=5
        )

    def test_purchase_str(self):
        self.assertEqual(
            str(self.purchase),
            f"testuser bought 5 of Sample Product"
        )

