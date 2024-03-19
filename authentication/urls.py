from django.urls import path
from .views import *

urlpatterns = [
    #path("profile", profile, name="profile"),
    path("customer_signup/",customer_signup,name="customer_signup"),
]