from django.db import models

# Create your models here.
from django.db import models
class Todo(models.Model):
    PRIORITY=(
        (1,"High"),
        (2,"Medium"),
        (3,"Low")
    )
    STATUS=(
        ('w',"Waiting"),
        ('p',"In Progress"),
        ('d',"Done")
    )
    title=models.CharField(max_length=20)
    description=models.TextField(null=True)
    priority=models.IntegerField(choices=PRIORITY,default=2)
    status=models.CharField(choices=STATUS,default='w',max_length=1)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    updated_date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return  f"{self.priority} - {self.title}"