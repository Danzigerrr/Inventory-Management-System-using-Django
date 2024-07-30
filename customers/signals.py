from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer


@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance, created, **kwargs):
    if created:
        # Create a new Customer profile
        Customer.objects.create(user=instance)
    else:
        # Update the Customer profile
        instance.customer_profile.save()
        