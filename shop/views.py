from django.shortcuts import render

# Create your views here.
def index(request):
        context = {"title":"SHOP"}
        return render(request, "shop/index.html", context)

def cart(request):
        context = {"title":"CART"}
        return render(request, "shop/cart.html", context)

def checkout(request):
        context = {"title":"CHECKOUT"}
        return render(request, "shop/checkout.html", context)