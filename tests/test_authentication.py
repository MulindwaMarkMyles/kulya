import pytest
from django.contrib.auth.models import User
from authentication.models import Customer, Business, Profile
from shop.models import Product, Category, Order, OrderItem, ShippingAddress

# @pytest.mark.django_db
# def test_product(new_product):
#     product = new_product
#     print("product:", product.name)
#     print("product:", product.image)
#     assert True

def test_user(new_user):
    user = new_user
    assert User.objects.filter(username=user.username).exists()
    
def test_customer(new_customer):
    customer = new_customer
    assert Customer.objects.filter(first_name=customer.first_name).exists()
    
def test_order(new_order):
    order = new_order
    assert Order.objects.filter(complete=order.complete, transaction_id=order.transaction_id).exists()
    
def test_orderitem(new_orderitem):
    orderitem = new_orderitem
    assert OrderItem.objects.count() == 1
    
def test_shippingaddress(new_shippingaddress):
    shippingaddress = new_shippingaddress
    assert ShippingAddress.objects.count() == 1

def test_product(new_product):
    product = new_product
    assert Product.objects.filter(name=product.name, owner=product.owner).exists()

def test_profile(new_profile):
    profile = new_profile
    assert Profile.objects.filter(user=profile.user).exists()
     