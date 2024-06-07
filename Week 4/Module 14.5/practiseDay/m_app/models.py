from django.db import models

# Create your models here.


class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    addess = models.TextField()
    file = models.FileField(upload_to='files/')
    # date_time_field = models.DateTimeField()
    # decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    # duration_field = models.DurationField()
    url = models.URLField()

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.email} {self.email} {self.addess} {self.file} {self.date_time_field} {self.decimal_field} {self.duration_field} {self.url}"
