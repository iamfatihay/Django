from django.db import models


class Student(models.Model):
    number=models.IntegerField()
    first_name=models.CharField(max_length=30) #! charfield kullanildiginda max_length vermek zorundayiz.
    last_name=models.CharField(max_length=40)
    comment=models.TextField()

# Eger burada model olusturuyorsan once "python manage.py makemigrations",
# daha sonra "python manage.py migrate" komutunu calistiriyoruz