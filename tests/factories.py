import factory, faker
from django.contrib.auth.models import User
from shop.models import *
from authentication.models import *

fake = faker.Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    is_superuser = True
    is_staff = True
    
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    category_name = factory.Faker("word")
    
class BusinessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Business
        
    owner = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    business_name = factory.Faker('company')
    email = fake.email()
    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = factory.Faker('word')
    description = factory.Faker('text')
    owner = factory.SubFactory(BusinessFactory)
    price = f"{fake.random_int()}"
    digital = factory.Faker('boolean')
    image = factory.Faker('image_url')
    category = factory.SubFactory(CategoryFactory)
    
    