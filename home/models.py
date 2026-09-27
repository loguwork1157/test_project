from django.db import models

# Create your models here.

class TestData(models.Model):
    name = models.CharField(max_length=20)
    value = models.IntegerField()
    

