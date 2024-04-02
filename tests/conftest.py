from pytest_factoryboy  import register
from .factories import *

register(UserFactory)
register(BusinessFactory)
register(ProductFactory)
register(CategoryFactory)
register(OrderFactory)
register(OrderItemFactory)