from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    #* Bu profile kime ait ve user silindiginde profile da silinsin
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #* Image kullaniyorsan , pip install Pillow
    image = models.ImageField(upload_to="pictures", default="pictures/avatar.png")
    # documents=models.FileField(upload_to="files")   ornek olarak
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

















#! Eger djangoun kendi user modelini kullanmayacaksaniz
#! asagadaki gibi AbstractUser dan inherit edip kendi modelinizi olusturabulirsiniz
#! settings.py a yeni user u tanimlamak gerekir.
#* # AUTH_USER_MODEL = 'users.MyUser'  

# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date


# class MyUser(AbstractUser):
#     username = models.CharField(max_length=50, blank=True, null=True, unique=True)
#     email = models.EmailField(("email address"), unique=True)
#     native_name = models.CharField(max_length=5)
#     phone_no = models.CharField(max_length=10)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username", "first_name", "last_name"]

#     def __str__(self):
#         return "{}".format(self.email)
