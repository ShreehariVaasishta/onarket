from django.dispatch import receiver
from core.models import User, Buyer
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_buyer(sender, instance, created, **kwargs):
    if created:
        """By default, the user is a buyer"""
        Buyer.objects.create(
            user=instance,
        )
