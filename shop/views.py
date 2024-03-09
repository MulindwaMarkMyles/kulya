from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

def index(request):
        products = Product.objects.all()
        context = {
                "title":"SHOP", 
                "products":products,
                }
        return render(request, "shop/index.html", context)

def cart(request):
        if request.user.is_authenticated:
                customer = request.user.customer
                order , created = Order.objects.get_or_create(customer=customer, complete=False)
                items = order.orderitem_set.all()
        else:
                items = []
                order = {'get_cart_total':0, 'get_cart_items':0}
                
        context = {"title":"CART", "items":items, "order": order}
        return render(request, "shop/cart.html", context)

def checkout(request):
        if request.user.is_authenticated:
                customer = request.user.customer
                order , created = Order.objects.get_or_create(customer=customer, complete=False)
                items = order.orderitem_set.all()
        else:
                items = []
                order = {'get_cart_total':0, 'get_cart_items':0}
                
        context = {"title":"CHECKOUT", "items":items, "order":order}
        return render(request, "shop/checkout.html", context)

def updateitem(request):
        data = json.loads(request.body)
        productId = data.get('productId')
        action = data.get('action')
        print(action , productId)
        
        customer = request.user.customer
        product = product.objects.get(id=productId)
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        return JsonResponse("Item was added.", safe=False)