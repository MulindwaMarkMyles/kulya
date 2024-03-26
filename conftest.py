import pytest

from pytest_factoryboy import register
from tests import factories

register(factories.CustomerFactory)

@pytest.fixture
def new_user(db, customer_factory):
    return customer_factory.create()