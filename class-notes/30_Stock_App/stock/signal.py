from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Purchases

# signal kullanınca admin etanıt
@receiver(pre_save, sender=Purchases)
def calculate_total_price(sender, instance, **kwargs):
    instance.price_total=instance.quantity*instance.price