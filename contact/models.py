from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.IntegerField()
    Address = models.TextField()
    created_date = models.DateField(auto_now_add=True)
