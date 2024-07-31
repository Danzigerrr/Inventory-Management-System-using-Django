from django.test import TestCase
from django.urls import reverse
from .utils import create_sample_data


class SalesReportViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        create_sample_data()

    def setUp(self):
        self.client.login(username='admin', password='adminpassword')

    def test_sales_report_accessible_by_admin(self):
        response = self.client.get(reverse('sales_report'))
        self.assertEqual(response.status_code, 200)

    def test_sales_report_inaccessible_by_non_admin(self):
        self.client.logout()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('sales_report'))
        self.assertEqual(response.status_code, 403)

    def test_sales_report_contains_correct_data(self):
        response = self.client.get(reverse('sales_report'))
        self.assertContains(response, '$70.00')  # total sales
        self.assertContains(response, 'Product1')
        self.assertContains(response, 'Product2')


class CustomerReportViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        create_sample_data()

    def setUp(self):
        self.client.login(username='admin', password='adminpassword')

    def test_customer_report_accessible_by_admin(self):
        response = self.client.get(reverse('customer_report'))
        self.assertEqual(response.status_code, 200)

    def test_customer_report_inaccessible_by_non_admin(self):
        self.client.logout()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('customer_report'))
        self.assertEqual(response.status_code, 403)

    def test_customer_report_contains_correct_data(self):
        response = self.client.get(reverse('customer_report'))
        self.assertContains(response, 'Test User')
        self.assertContains(response, 'Product1')
        self.assertContains(response, 'Product2')


class InventoryReportViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        create_sample_data()

    def setUp(self):
        self.client.login(username='admin', password='adminpassword')

    def test_inventory_report_accessible_by_admin(self):
        response = self.client.get(reverse('inventory_report'))
        self.assertEqual(response.status_code, 200)

    def test_inventory_report_inaccessible_by_non_admin(self):
        self.client.logout()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('inventory_report'))
        self.assertEqual(response.status_code, 403)

    def test_inventory_report_contains_correct_data(self):
        response = self.client.get(reverse('inventory_report'))
        self.assertContains(response, 'Product1')
        self.assertContains(response, '50')

