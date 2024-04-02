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
        profile = profile_factory(image=image_path)
        assert profile.imageurl != image_path
        
    def test_save_method(self, profile_factory):
        image = faker.Faker().image_url().replace("https://","")
        image = image.replace("/","") + ".jpg"
        profile = profile_factory(image=image)
        print(image)
        print(profile.image.name)
        assert profile.image.name != image