import factory, faker
from django.contrib.auth.models import User
from shop.models import *
from authentication.models import *

fake = faker.Faker()

#authentication factories

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    is_superuser = True
    is_staff = True

class BusinessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Business
        
    owner = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    business_name = factory.Faker('company')
    email = fake.email()

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
        
    user = factory.SubFactory(UserFactory)
    image = fake.image_url()
    
class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
        
    user = factory.SubFactory(UserFactory)
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    
#shop factories
    
    
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    category_name = factory.Faker("word")
    
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
    
class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
    
    customer = factory.SubFactory(UserFactory)
    complete = fake.boolean()
    transaction_id = fake.random_number()
    
class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem
    
    product = factory.SubFactory(ProductFactory)
    order = factory.SubFactory(OrderFactory)
    quantity = 0

class ShippingAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShippingAddress
    
    customer = factory.SubFactory(UserFactory)
    order = factory.SubFactory(OrderFactory)
    address = fake.address()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()
    
