from django.db import models

# Create your models here.
class Car(models.Model):
    plate_number=models.CharField(max_length=20, unique=True)