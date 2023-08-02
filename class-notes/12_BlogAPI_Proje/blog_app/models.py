from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(null=True, max_length=100)
    content=models.TextField(null=True)
    created_date=models.DateTimeField(auto_now_add=True, null=True) #! Ilk task eklenirken eklenir sadece
    updated_date=models.DateTimeField(auto_now=True)  #! her islem degisikliginde tarih ekler

    def __str__(self):   #! Admin panelde nasil gorecegimizi belirliyoruz.
        return f"{self.title}"
    
    # class Meta:   
    #     ordering=["priority"]


