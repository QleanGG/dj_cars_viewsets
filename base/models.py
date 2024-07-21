from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.IntegerField()
    brand = models.CharField(max_length=50,null=True,blank=True)
    color = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.color}"
    
