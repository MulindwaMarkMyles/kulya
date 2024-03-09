from django.db import models
from authentication.models import Customer, Business
        
class Product(models.Model):
        name = models.CharField(max_length=100)
        owner = models.ForeignKey(Business, on_delete=models.CASCADE,null=True)
        price = models.FloatField()
        digital = models.BooleanField(default=False)
        image = models.ImageField(null=True, blank=True)
        
        def __str__(self):
                return f"{self.name} costs {self.price}"
        
        @property
        def imageurl(self):
                try:
                        url = self.image.url
                except:
                        url = ''
                return url
        
class Order(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
        date_ordered = models.DateTimeField(auto_now_add=True)
        complete = models.BooleanField(default=False)
        transaction_id = models.CharField(max_length=100)
        
        def __str__(self):
                return f"{self.id}"
        
        @property
        def get_cart_total(self):
                orderitems = self.orderitem_set.all()
                total = sum([item.get_total for item in orderitems])
                return total
        
        @property
        def get_cart_items(self):
                orderitems = self.orderitem_set.all()
                total = sum([item.quantity for item in orderitems])
                return total
        
class OrderItem(models.Model):
        product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
        order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
        quantity = models.IntegerField(default=0)
        date_added = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
                return "{0} by {1}".format(self.product.name, self.order.customer.name ) 
        
        @property
        def get_total(self):
                total = self.product.price * self.quantity
                return total
        
class ShippingAddress(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
        order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
        address = models.CharField(max_length=50)
        city = models.CharField(max_length=50)
        state = models.CharField(max_length=50, null=True)
        zipcode = models.CharField(max_length=50, null=True)
        date_added = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
                return self.address
        
        