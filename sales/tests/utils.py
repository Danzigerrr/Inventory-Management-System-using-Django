from django.contrib.auth.models import User
from sales.models import Product
from users.models import Customer
from inventory.models import Purchase


def create_sample_data():
    user = User.objects.create_user(username='testuser', password='testpassword')
    admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
    product1 = Product.objects.create(name='Product1', price=10.00, stock=50)
    product2 = Product.objects.create(name='Product2', price=20.00, stock=30)
    customer = Customer.objects.create(user=user, name='Test User', email='testuser@example.com', phone='1234567890')
    Purchase.objects.create(user=user, product=product1, quantity=3)
    Purchase.objects.create(user=user, product=product2, quantity=2)
    return user, admin_user, product1, product2, customer
