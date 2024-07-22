from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25, null=False)
    roll = models.IntegerField(null=False)
    city = models.CharField(max_length=50, null= False)

    def __str__(self):
        return self.name