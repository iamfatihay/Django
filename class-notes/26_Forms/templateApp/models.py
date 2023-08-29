from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER=(
        ("M", "Male"),
        ("F", "Female")
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    picture= models.ImageField(upload_to='profile_pictures', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"