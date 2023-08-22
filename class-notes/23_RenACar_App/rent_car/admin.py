from django.contrib import admin

# Register your models here.
from .models import Reservation, Car
admin.site.register(Reservation)
admin.site.register(Car)
