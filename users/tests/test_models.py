from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Customer


class CustomerModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )
        self.customer = Customer.objects.create(
            user=self.user,
            name='Test User',
            email='testuser@example.com',
            phone='123-456-7890'
        )

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'Test User')

    def test_customer_unique_email(self):
        # Test that email uniqueness is enforced
        with self.assertRaises(Exception):
            Customer.objects.create(
                user=User.objects.create_user(
                    username='anotheruser',
                    password='anotherpassword',
                    email='testuser@example.com'
                ),
                name='Another User',
                email='testuser@example.com',
                phone='098-765-4321'
            )
