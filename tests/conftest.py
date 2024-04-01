from pytest_factoryboy  import register
from .factories import UserFactory, BusinessFactory, ProductFactory

register(UserFactory)
register(BusinessFactory)
register(ProductFactory)