import pytest
from faker import Faker

fake = Faker()

# @pytest.mark.parametrize(
#     "name, description, price, digital, image, rating",
#     [
#         (fake.name(), fake.text(), "10000.00", fake.boolean(),fake.image_url(), 5.0),
#         (fake.name(), fake.text(), "810000.00", fake.boolean(),fake.image_url(), 10.0),
#         (fake.name(), fake.text(), "840000.00", fake.boolean(),fake.image_url(), 14.0),
#         (fake.name(), fake.text(), "90000.00", fake.boolean(),fake.image_url(), 18.0),
#     ],
# )
# def test_product(db, product_factory, name, description, price, digital, image, rating):
#     product = product_factory(name=name, description=description, price=price, digital=digital, image=image, rating=rating)
#     assert product.name == name
#     assert product.description == description
#     assert product.price == price
#     assert product.digital == digital
#     assert product.rating == rating