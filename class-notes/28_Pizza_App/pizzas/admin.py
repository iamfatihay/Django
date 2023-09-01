from django.contrib import admin
from .models import Toppings, Order, Pizza

# Register your models here.
admin.site.register(Toppings)
admin.site.register(Order)
admin.site.register(Pizza)