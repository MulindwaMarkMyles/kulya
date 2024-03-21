from django.urls import path
from .views import *

urlpatterns = [
    path("profile", profile, name="profile"),
    path("customer_signup/",customer_signup,name="customer_signup"),
    path("Sign_Up/",Sign_Up, name= "Sign_Up"),
    path("business_signup/", business_signup, name="business_signup"),
]