from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os, uuid


def rename_image(instance, form_picture):
    _, f_ext = os.path.splitext(form_picture)
    new_file_name = "%s%s" % (uuid.uuid4(), f_ext)
    return new_file_name

class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        image = models.ImageField(default="default-4.jpg", upload_to="profile_pics")
        
        def __str__(self):
                return f"{self.user.username} Profile."
        
        @property
        def imageurl(self):
            try:
                url = self.image.url
            except:
                url = ""
            return url
        
        def save(self, *args, **kwargs):
                if self.image.name != "default-4.jpg":
                    self.image.name = rename_image(self, self.image.name)
                super().save(*args, **kwargs)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    email = models.EmailField()

    @property
    def name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return f"{self.name}"


class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    business_name = models.CharField(max_length=300, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.business_name}"
