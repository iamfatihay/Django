from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile

#* User olustuktan sonra token da olussun istiyoruz
#* Signal.py dosyasi pre ve post save gibi islemlerde kullanilir, burada mesela
#* User oliusturulup save edildiginde Profil de olussun istiyoruz. !!!

@receiver(post_save, sender=User)
def create_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)



# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created=False, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
