from django.db import models
from inventory.models import Product


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.product.stock -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)
