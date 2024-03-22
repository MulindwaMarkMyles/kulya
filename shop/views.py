from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utilities import *
#from django.froms import inlineformset_factory
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
# Create your views here.

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
    print(action, productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
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

def profile(request):
    context={
        'title':'Uer Profile',
        'name':'USER NAME',
        'email':'USER EMAIL',
        'phone_number':'PHONE NUMBER'
         }

    return render(request, "shop/login.html",context) 


def login(request):

    return render(request, "shop/login.html")  

def signup(request):
    form = UserCreationForm()
   
    if request.methode == 'post':
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()
    context= {'form': form}

    return render(request, "shop/signup.html", context) 