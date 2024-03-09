from django.shortcuts import render
from .models import *

def index(request):
        products = Product.objects.all()
        context = {
                "title":"SHOP", 
                "products":products,
                }
        return render(request, "shop/index.html", context)

def cart(request):
        context = {"title":"CART"}
        return render(request, "shop/cart.html", context)

def checkout(request):
        context = {"title":"CHECKOUT"}
        return render(request, "shop/checkout.html", context)