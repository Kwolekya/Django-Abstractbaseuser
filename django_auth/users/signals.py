from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from users.models import Customer

@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='create_customer')
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(customer=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='save_customer')
def save_customer(sender, instance, **kwargs):
    instance.customer.save()