from django.urls import path
from .views import *

urlpatterns = [
        path('', index, name="shop"),
        path('cart/', cart, name="cart"),
        path('checkout/', checkout, name="checkout"),
        path('update-item/', updateitem, name="update-item"),
        path('process-order/', processOrder, name="process-order"),
        path('profile/',profile, name="profile"),
        path('login/', login,name='login'),
        path('loginn/', login, name='loginn'), 
        path('product-view/<int:id>', viewProduct, name="view-product"),
]

