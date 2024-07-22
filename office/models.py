from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Patient(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    heart = models.IntegerField(default=73, validators=[MinValueValidator(1),MaxValueValidator(300)])

    def __str__(self):
         return f"{self.fName} {self.lName} is {self.age} years old"