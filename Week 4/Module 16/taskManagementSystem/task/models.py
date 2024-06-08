from django.db import models

# Create your models here.


class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date = models.DateField()

    def __str__(self):
        return self.taskTitle
