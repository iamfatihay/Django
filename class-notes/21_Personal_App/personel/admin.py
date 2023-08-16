from django.contrib import admin

# Register your models here.
from .models import Department,Personel, Profile
admin.site.register(Department)
admin.site.register(Personel)
admin.site.register(Profile)
