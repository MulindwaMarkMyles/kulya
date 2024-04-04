import pytest
import faker

pytestmark = pytest.mark.django_db

class TestProfileModel:
    def test_str_return(self, profile_factory, user_factory):
        user = user_factory(username="mulin")
        profile = profile_factory(user=user)
        assert profile.__str__() == "mulin Profile."
        
    def  test_imageurl_return(self, profile_factory):
        image_path = faker.Faker().image_url()
        profile_one = profile_factory(image=image_path)
        
        assert profile_one.imageurl != image_path
        
    def test_save_method(self, profile_factory):
        image = faker.Faker().image_url().replace("https://","")
        image = image.replace("/","") + ".jpg"
        profile = profile_factory(image=image)
        assert profile.image.name != image
        
class TestCustomerModel:
    def test_name_return(self, customer_factory):
        customer = customer_factory(first_name="Sulaiman", last_name="Ashley")
        assert customer.name == "Sulaiman Ashley"
    
    def test_str_return(self, customer_factory):
        customer = customer_factory(first_name="Sulaiman", last_name="Ashley")
        assert customer.__str__() == "Sulaiman Ashley"
        
class TestBusinessModel:
    def test_str_return(self, business_factory):
        company = faker.Faker().company()
        business = business_factory(business_name=company)
        assert business.__str__() == company