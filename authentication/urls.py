from django.urls import path
from .views import *

urlpatterns = [
     path("profile/", profile, name="profile"),
    path('login/', login_user,name='login'),
    path('signup-u/', signup_user, name="signup"),  
    path('signup-b/', signup_business, name="signup-b"),  
    path('logout/', logout_u, name="logout"),  
    path('add-products/', add_products, name="add-products"),  
    path('Ts&Cs/', terms_conditions, name="tsandcs") 
]
