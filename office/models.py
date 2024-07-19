from django.db import models

# Create your models here.
class Patient(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    age = models.IntegerField()
