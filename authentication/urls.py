from django.urls import path
from shop.urls import *
from .views import *

urlpatterns = [
    path("profile/", profile, name="profile"),
    path('login/', login,name='login'),
    path('checkout/', checkout, name="checkout"),

]
