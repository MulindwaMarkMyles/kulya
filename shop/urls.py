from django.urls import path
from .views import *

urlpatterns = [
        path('', index, name="home"),
        path('shop/', shop, name="shop"),
        path('cart/', cart, name="cart"),
        path('checkout/', checkout, name="checkout"),
        path('update-item/', updateitem, name="update-item"),
        path('process-order/', processOrder, name="process-order"),
        path('product-view/<int:id>', viewProduct, name="view-product"),
        path('about/', about, name="about"),
]

