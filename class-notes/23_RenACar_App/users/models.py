from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # bu profile kime ait ve user silindiğinde profileda silinsin
    image=models.ImageField(upload_to="pictures",default="/pictures/avatar.png" )
    # documents=models.FileField(upload_to="files")
    #image kullanıyorsan pip install Pillow

    about=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}"    


# Create your models here.







# EĞER djangon un kendi user modelini kullanmayacaksanız 
# aşağıdaki gibi abstructuserdan inherit edip kendi modelinizi olşturabilirisniz
# settings.py a yeni  modeli belirtin        AUTH_USER_MODEL = 'users.MyUser'

    
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date
# class MyUser(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(('email address'), unique = True)
#   native_name = models.CharField(max_length = 5)
#   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  
#   def __str__(self):
#       return "{}".format(self.email)