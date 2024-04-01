import pytest

pytestmark = pytest.mark.django_db

class TestProductModel:
    def  test_str_return(self, product_factory):
        product = product_factory(name="pods", price="4342.1")
        assert product.__str__() == "pods costs 4342.1"