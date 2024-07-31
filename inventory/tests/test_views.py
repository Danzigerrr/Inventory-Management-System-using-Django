from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Product, InventoryTransaction, Purchase
from ..forms import InventoryTransactionForm, ProductForm, PurchaseForm


class InventoryViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(username='admin', password='adminpassword')
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.product = Product.objects.create(
            name='Sample Product',
            price=10.99,
            stock=100
        )
        cls.inventory_transaction = InventoryTransaction.objects.create(
            product=cls.product,
            transaction_type='RECEIVE',
            quantity=10
        )

    def setUp(self):
        self.client.login(username='admin', password='adminpassword')

    def test_manage_inventory_accessible_by_admin(self):
        response = self.client.get(reverse('manage_inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Manage Inventory')

    def test_add_product_accessible_by_admin(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add Product')

    def test_search_products_accessible(self):
        response = self.client.get(reverse('search_products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Search Products')

    def test_buy_product_accessible(self):
        response = self.client.get(reverse('buy_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buy Product')

    def test_purchased_products_accessible(self):
        Purchase.objects.create(user=self.user, product=self.product, quantity=5)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('purchased_products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Purchased Products')
        self.assertContains(response, 'Sample Product')

    def test_manage_inventory_transaction(self):
        self.client.post(reverse('manage_inventory'), {
            'product': self.product.id,
            'transaction_type': 'SELL',
            'quantity': 5
        })
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 95)

    def test_manage_inventory_insufficient_stock(self):
        response = self.client.post(reverse('manage_inventory'), {
            'product': self.product.id,
            'transaction_type': 'SELL',
            'quantity': 200
        })
        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 100)  # Stock should not change

    def test_add_product(self):
        response = self.client.post(reverse('add_product'), {
            'name': 'New Product',
            'price': 20.99,
            'stock': 50
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Product.objects.filter(name='New Product').exists())
