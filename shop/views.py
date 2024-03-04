from django.shortcuts import render

# Create your views here.
def index(request):
        context = {}
        return render(request, "shop/index.html", context)

def cart(request):
        context = {}
        return render(request, "shop/cart.html", context)

def checkout(request):
        context = {}
        return render(request, "shop/checkout.html", context)