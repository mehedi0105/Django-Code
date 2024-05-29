from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    addess = models.TextField()
    father_name = models.TextField(default='Rahim')

    def __str__(self) -> str:
        return f"{self.roll} {self.name} {self.addess} {self.father_name}"


class StudetModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
