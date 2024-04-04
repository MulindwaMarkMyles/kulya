from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

def test_profile(client):
    response = client.get(reverse('profile'))
    assert response.status_code == 302

def test_login_user(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/login.html")
    
def test_signup_user(client):
    response = client.get(reverse('signup'))
    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/signup-user.html")
    
def test_signup_business(client):
    response = client.get(reverse('signup-b'))
    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/signup-business.html")

def test_logout_u(client):
    response = client.get(reverse('logout'))
    assert response.status_code == 302
