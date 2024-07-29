from django.db import models


# Create your models here.
class Teacher(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.fName} {self.lName} teaches {self.subject}"
