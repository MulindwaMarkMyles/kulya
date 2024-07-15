from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os, uuid



# Function to rename uploaded image files
def rename_image(instance, form_picture):
    _, f_ext = os.path.splitext(form_picture)
    new_file_name = "%s%s" % (uuid.uuid4(), f_ext)
    return new_file_name

# Profile model representing user profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model
    image = models.ImageField(default="default-4.jpg", upload_to="profile_pics")  # Image field for profile picture

    def __str__(self):
        return f"{self.user.username} Profile."  # String representation of the profile

    # Property to get the image URL
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    # Override save method to rename image file
    def save(self, *args, **kwargs):
        if self.image.name != "default-4.jpg" and not self.id:
            self.image.name = rename_image(self, self.image.name)
        super().save(*args, **kwargs)

# Customer model representing customers in the system
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)  # Link to User model
    first_name = models.CharField(max_length=300, null=True)  # First name field
    last_name = models.CharField(max_length=300, null=True)  # Last name field
    email = models.EmailField()  # Email field
    verified = models.BooleanField(default=False)
    phone_number = models.IntegerField(null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    # Property to get the full name of the customer
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.name}"  # String representation of the customer

# Business model representing businesses in the system
class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)  # Link to User model
    first_name = models.CharField(max_length=300, null=True)  # First name field
    last_name = models.CharField(max_length=300, null=True)  # Last name field
    business_name = models.CharField(max_length=300, null=True)  # Business name field
    email = models.EmailField()  # Email field
    verified = models.BooleanField(default=False)
    phone_number = models.IntegerField(null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f"{self.business_name}"  # String representation of the business
        

class Chat(models.Model):
    the_customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customer')
    the_business = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Business', null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class GroupChatMessages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE, null=True, blank=True)
