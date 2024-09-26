from django.db import models

# Create your models here.
class Student1(models.Model):
    name1=models.CharField(max_length=60)
    place1=models.CharField(max_length=20)
    phone=models.IntegerField()
    def __str__(self):
       return self.name1