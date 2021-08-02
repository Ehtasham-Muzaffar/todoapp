from django.db import models

# Create your models here.
class tododata(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)

    def __str__(self):
        return self.name