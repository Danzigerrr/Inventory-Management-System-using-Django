from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class InventoryTransaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=[('IN', 'In'), ('OUT', 'Out')])
    date = models.DateTimeField(auto_now_add=True)
