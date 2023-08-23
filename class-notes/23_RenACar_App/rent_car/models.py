from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Car(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=20)
    rent_per_day = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return  f"{self.brand} - {self.model} - {self.rent_per_day}"
    

class Reservation(models.Model):
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return  f"{self.car.plate_number} - {self.customer} - {self.end_date}"

