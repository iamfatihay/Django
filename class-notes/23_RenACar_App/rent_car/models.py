from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DAY=(
    (1,"one day"),
    (2,"two days"),
    (3,"three days"),
    (4,"four days"),
    (5,"five days"),
    (6,"six days"),
    (7,"seven days"),
)

class Car(models.Model):

    plate_number=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    year=models.SmallIntegerField()
    gear=models.CharField(max_length=30) 
    rent_per_day=models.CharField(max_length=1,choices=DAY)
    availability=models.BooleanField()
    
    def __str__(self):
        return  f"{self.plate_number} {self.brand} {self.rent_per_day}"
    

class Reservation(models.Model):
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name