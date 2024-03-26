import pytest

from pytest_factoryboy import register
from tests import factories

register(factories.CustomerFactory)
register(factories.ProductFactory)
register(factories.BusinessFactory)

@pytest.fixture
def new_user(db, customer_factory):
    return customer_factory.create()

@pytest.fixture
def new_product(db, product_factory):
    return product_factory.create()