import pytest

from pytest_factoryboy import register
from tests import factories

register(factories.CustomerFactory)
register(factories.ProductFactory)
register(factories.UserFactory)
register(factories.ProfileFactory)
register(factories.OrderFactory)
register(factories.OrderItemFactory)
register(factories.AddressFactory)

@pytest.fixture
def new_customer(db, customer_factory):
    return customer_factory.create()

@pytest.fixture
def new_user(db, user_factory):
    return user_factory.create()

@pytest.fixture
def new_order(db, order_factory):
    return order_factory.create()

@pytest.fixture
def new_orderitem(db, order_item_factory):
    return order_item_factory.create()

@pytest.fixture
def new_shippingaddress(db, address_factory):
    return address_factory.create()

@pytest.fixture
def new_product(db, product_factory):
    return product_factory.create()

@pytest.fixture
def new_profile(db, profile_factory):
    return profile_factory.create()