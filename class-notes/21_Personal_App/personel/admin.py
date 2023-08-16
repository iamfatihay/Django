from django.contrib import admin

# Register your models here.
from .models import Department,Personel
admin.site.register(Department)
admin.site.register(Personel)
