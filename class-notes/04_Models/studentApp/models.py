from django.db import models


class Student(models.Model):
    COHORTS=[
        ('FS','FullStack'),
        ('DS','DataScience'),
        ('AWS','AWS DevOps'),
    ]
    number=models.IntegerField()
    first_name=models.CharField(max_length=30) #! charfield kullanildiginda max_length vermek zorundayiz.
    last_name=models.CharField(max_length=40)
    comment=models.TextField(null=True)
    register_date=models.DateTimeField(auto_now_add=True, null=True)
    updated_date=models.DateTimeField(auto_now=True, null=True)
    is_active=models.BooleanField(default=True)
    cohort=models.CharField(max_length=3, choices=COHORTS, default='FS')
    email=models.EmailField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering=["first_name"]  #* basina "-" koyarsak siralamayi tersine cevirir.
        verbose_name_plural="ögrenciler"  #* admin paneldeki class ismini degistirmis oluyoruz.



# Eger burada model olusturuyorsan once "python manage.py makemigrations",
# daha sonra "python manage.py migrate" komutunu calistiriyoruz