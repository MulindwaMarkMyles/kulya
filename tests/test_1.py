import pytest
from django.contrib.auth.models import User
from authentication.models import Customer

# @pytest.mark.django_db
# def test_new_user(new_user):
#     customer = new_user
#     count = Customer.objects.count()
#     print(count)
#     print("customer_factory", customer.first_name)
#     print("customer_factory", customer.email)
#     assert True

@pytest.mark.django_db
def test_product(new_product):
    product = new_product
    print("product:", product.name)
    print("product:", product.image)
    assert True
     