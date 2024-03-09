from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"


class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    business_name = models.CharField(max_length=300, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.business_name}"
