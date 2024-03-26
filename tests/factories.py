import factory
from faker import Faker

fake = Faker()

from authentication.models import Customer, Business
from shop.models import Product, Category

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    first_name = fake.name()
    email = fake.email()
    
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = "shoppie"

class BusinessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Business
        
    first_name = fake.name()
    email = fake.email()
    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = "product name"
    description = fake.text()
    owner = factory.SubFactory(BusinessFactory)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    digital = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, max_length=500)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    rating = models.DecimalField(default=0.0, decimal_places=1, max_digits=3)
    