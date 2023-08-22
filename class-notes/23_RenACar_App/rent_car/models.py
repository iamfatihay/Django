from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    plate_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    gear = models.CharField(max_length=20)
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return  f"{self.id} {self.plate_number} {self.rent_per_day}"
    

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return  f"{self.car} {self.customer} {self.end_date}"

