from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        city = models.CharField(max_length=100)
        village = models.CharField(max_length=100)
        phone_number = models.IntegerField()
        
        def __str__(self):
                return self.user.username
        
class BusinessOwner(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        business_name = models.CharField(max_length=50)
        city = models.CharField(max_length=100)
        village = models.CharField(max_length=100)
        phone_number = models.IntegerField()
        alternative_phone_number = models.IntegerField()
        
        def __str__(self):
                return self.business_name




        

