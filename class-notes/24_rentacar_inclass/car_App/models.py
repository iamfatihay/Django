from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import date


# Create your models here.
class Car(models.Model):
    GEAR = (
        ("a", "automatic"),
        ("m", "manual"),
    )
    plate_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=20, choices=GEAR)
    rent_per_day = models.DecimalField(
        max_digits=8, decimal_places=3, validators=[MinValueValidator(50)]
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} - {self.model}"
    

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations_customer")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="reservations_car")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.customer} - {self.car.plate_number} - {self.start_date} - {self.end_date}"
