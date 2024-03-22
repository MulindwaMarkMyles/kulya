from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utilities import *


def index(request):
    data = cartData(request)
    cartItems = data["cartItems"]

    products = Product.objects.all()
    context = {
        "title": "SHOP",
        "range": range(5),
        "products": products,
        "cartItems": cartItems,
        "shipping": False,
    }
    return render(request, "shop/index.html", context)


def cart(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    context = {
        "title": "CART",
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "shipping": False,
    }
    return render(request, "shop/cart.html", context)


def checkout(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    context = {
        "title": "CHECKOUT",
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "shipping": False,
    }
    return render(request, "shop/checkout.html", context)


def updateitem(request):
    data = json.loads(request.body)
    productId = data.get("productId")
    action = data.get("action")
    

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order = Order.objects.filter(customer=customer, complete=False).first()
    if order == None:
        order = Order.objects.create(customer=customer, complete=False)    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was added.", safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data["form"]["total"])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data["shipping"]["address"],
            city=data["shipping"]["city"],
            state=data["shipping"]["state"],
            zipcode=data["shipping"]["zipcode"],
        )

    return JsonResponse("Payment completed.", safe=False)

def profile(request):
    context={
        'title':'Uer Profile',
        'name':'USER NAME',
        'email':'USER EMAIL',
        'phone_number':'PHONE NUMBER'
         }

    return render(request, "shop/profile.html",context)  

def login(request):

    return render(request, "shop/login.html") 


def viewProduct(request, id):
    product = Product.objects.filter(id=id).first()
    data = cartData(request)
    try:
        quantity = data["items"].filter(product=product).first().quantity
    except:
        quantity = 0
    cartItems = data["cartItems"]
    context = {"product": product, "cartItems": cartItems, "title":"PRODUCT", "quantity": quantity}
    return render(request, "shop/product.html", context)

def about(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    return render(request, "shop/about.html", {"title":"ABOUT", "cartItems": cartItems})