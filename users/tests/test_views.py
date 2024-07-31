from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Customer


class UserViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        cls.customer = Customer.objects.create(
            user=cls.user,
            name='Test User',
            email='testuser@example.com',
            phone='123-456-7890'
        )

    def setUp(self):
        self.client.login(username='testuser', password='testpassword')

    def test_register_accessible(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')

    def test_register_valid_post(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'ComplexP@ssword123',
            'password2': 'ComplexP@ssword123',
            'email': 'newuser@example.com',
            'name': 'New User',
            'phone': '1234567890'
        })

        # Check if the form submission was successful
        self.assertEqual(response.status_code, 302)  # Should redirect after successful registration
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_profile_accessible(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_shows_no_purchases(self):
        response = self.client.get(reverse('profile'))
        self.assertContains(response, 'No purchased products yet.')

    def test_profile_shows_purchases(self):
        # Create a purchase for the user
        from inventory.models import Product, Purchase
        product = Product.objects.create(name='Sample Product', price=10.99, stock=100)
        Purchase.objects.create(user=self.user, product=product, quantity=5)

        response = self.client.get(reverse('profile'))
        self.assertContains(response, 'Sample Product')
