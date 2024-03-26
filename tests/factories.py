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
        
    category_name = "shoppie"

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
    price = "10000.00"
    digital = fake.boolean()
    category = factory.SubFactory(CategoryFactory)
    image = fake.image_url()
    rating = 5.0
    