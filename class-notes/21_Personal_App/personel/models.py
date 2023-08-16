from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, null=True) #! Ilk task eklenirken eklenir sadece
    updated=models.DateTimeField(auto_now=True)  #! her islem degisikliginde tarih ekler

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name
    

class Personel(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender = models.IntegerField(null=True)
    title = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    started=models.DateTimeField()   
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, null=True) 
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Personel '
        verbose_name_plural = 'Personels '

    def __str__(self):  
        return f"{self.first_name} - {self.last_name}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
