from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Review(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

class Car(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"PK: {self.pk} - Car is {self.brand} {self.year}"