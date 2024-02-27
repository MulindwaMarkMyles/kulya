from django.db import models
from django.utils import timezone
from authentication.models import BusinessOwner
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
        owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        category = models.CharField(max_length=50)
        # images = models.ManyToManyField(ProductImage, related_name='product_images')

        def __str__(self):
                return self.name    
        
class ProductImage(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='product_images/')
        
        def __str__(self):
                return f"Image for {self.product.name}"
                

class Order(models.Model):
        customer = models.ForeignKey(User, on_delete=models.CASCADE)
        products = models.ManyToManyField(Product, through='OrderItem')
        order_date = models.DateTimeField(default=timezone.now)
        total_amount = models.IntegerField()
        

        def __str__(self):
                return f"Order #{self.id} by {self.customer.username}"


class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField()

        def __str__(self):
                return f"{self.quantity} x {self.product.name}"