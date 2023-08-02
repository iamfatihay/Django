from django.db import models
from django.conf import settings

class Blog(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_id=models.CharField(max_length=100)
    title=models.CharField(null=True, max_length=100)
    content=models.TextField(null=True)
    created_date=models.DateTimeField(auto_now_add=True, null=True) #! Ilk task eklenirken eklenir sadece
    updated_date=models.DateTimeField(auto_now=True)  #! her islem degisikliginde tarih ekler

    def __str__(self):   #! Admin panelde nasil gorecegimizi belirliyoruz.
        return f"{self.title}"
    
    # class Meta:   
    #     ordering=["priority"]
from django.db import models

# Create your models here.
