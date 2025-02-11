from django.urls import path
from .views import *
from authentication.views import groupchat

urlpatterns = [
        path('', index, name="home"),
        path('shop/', ShopView.as_view(), name="shop"),
        path('cart/', cart, name="cart"),
        path('checkout/', checkout, name="checkout"),
        path('update-item/', updateitem, name="update-item"),
        path('process-order/', processOrder, name="process-order"),
        path('product-view/<int:id>/', viewProduct, name="view-product"),
        path('product-view-p/<int:id>/', viewProductP, name="view-product-p"),
        path('delete-view/<int:id>/', deleteProduct, name="delete-product"),
        path('about/', about, name="about"),
        path('Ts&Cs/', terms_conditions, name="tsandcs"),
        path('offers/', offers, name="offers"),
        path('category/<str:category_name>/', category, name="category"),
        path('category-chat/<str:category_name>/', groupchat, name="category-chat"),
        path("payment-success/", paymentsuccessful, name="payment-success"),
        path("payment-failed/", paymentfailed, name="payment-failure"),
        path("delete-order/<int:pk>/", deleteOrder, name="delete-order"),
]

