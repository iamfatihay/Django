from django.contrib import admin

# Register your models here.
from .models import Department, Personnel
admin.site.register(Department)
admin.site.register(Personnel)