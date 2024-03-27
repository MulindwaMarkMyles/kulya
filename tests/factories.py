import factory
from faker import Faker
from authentication.models import Customer, Business, Profile
from shop.models import Product, Category, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    username = fake.name()
    email = fake.email()
    password = fake.name()

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    	
    user = factory.SubFactory(UserFactory)
    first_name = fake.name()
    last_name = fake.name()
    email = fake.email()
    
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    category_name = "shoppie"

class BusinessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Business
        
    owner = factory.SubFactory(UserFactory)
    first_name = fake.name()
    last_name = fake.name()
    business_name = fake.text()
    email = fake.email()
    
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
    
    user = factory.SubFactory(UserFactory)
    image = fake.image_url()
        
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
    
class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
        
    customer = factory.SubFactory(UserFactory)
    complete = False
    transaction_id = fake.text()

class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem
        
    # product = factory.SubFactory(ProductFactory)
    # order = factory.SubFactory(OrderFactory)
    quantity = fake.random_number(10)
    
class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShippingAddress
        
    # customer = factory.SubFactory(UserFactory)
    # order = factory.SubFactory(OrderFactory)
    address = fake.text()
    city = fake.text()
    state = fake.text()
    zipcode = fake.text()
    
    