from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        city = models.CharField(max_length=100)
        village = models.CharField(max_length=100)
        phone_number = models.IntegerField()
        
class 
