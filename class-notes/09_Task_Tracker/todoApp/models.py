from django.db import models

class Todo(models.Model):

    PRIORITY=(
        (1, "High"),
        (2, "Medium"),
        (3, "Low")
    )
    task=models.CharField(max_length=100)
    description=models.TextField(null=True)
    priority=models.IntegerField(choices=PRIORITY, default=2)
    created_date=models.DateTimeField(auto_now_add=True, null=True) #! Ilk task eklenirken eklenir sadece
    updated_date=models.DateTimeField(auto_now=True)  #! her islem degisikliginde tarih ekler
    is_done=models.BooleanField(default=False) 

    def __str__(self):   #! Admin panelde nasil gorecegimizi belirliyoruz.
        return f"{self.priority} - {self.task}"
    
    class Meta:   
        ordering=["priority"]
