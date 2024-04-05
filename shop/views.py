from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utilities import *
# Create your views here.

def index(request):
    # Retrieve cart data
    data = cartData(request)
    cartItems = data["cartItems"]
    
    # Retrieve all categories and recent products
    categories = Category.objects.all()
    products = Product.objects.order_by("-id")[:30]
    
    # Prepare context for rendering the index page
    context = {
        "title": "HOME",
        "range": range(5),
        "products": products,
        "cartItems": cartItems,
        "shipping": False,
        "categories": categories,
    }
    return render(request, "shop/index.html", context)

def shop(request):
    # Retrieve cart data
    data = cartData(request)
    cartItems = data["cartItems"]
    
    # Handle search functionality
    if request.method == 'POST':
        searchterm = request.POST.get("searchterm")
        products = Product.objects.filter(name__contains=searchterm)
    else:
        products = Product.objects.order_by("-id")[:]
        
    # Prepare context for rendering the shop page
    context = {
        "title": "SHOP",
        "range": range(5),
        "products": products,
        "cartItems": cartItems,
        "shipping": False,
    }
    return render(request, "shop/shop.html", context)

def cart(request):
    # Retrieve cart data
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    # Prepare context for rendering the cart page
    context = {
        "title": "CART",
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "shipping": False,
    }
    return render(request, "shop/cart.html", context)

def checkout(request):
    # Retrieve cart data
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    # Prepare context for rendering the checkout page
    context = {
        "title": "CHECKOUT",
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "shipping": False,
    }
    return render(request, "shop/checkout.html", context)

def updateitem(request):
    # Update item quantity in the cart
    data = json.loads(request.body)
    productId = data.get("productId")
    action = data.get("action")

    # Retrieve current user and product
    customer = request.user
    product = Product.objects.get(id=productId)
    
    # Retrieve or create order for the user
    order = Order.objects.filter(customer=customer, complete=False).first()
    if order == None:
        order = Order.objects.create(customer=customer, complete=False)    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    # Update quantity based on action
    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    # Delete order item if quantity is zero
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was added.", safe=False)

def processOrder(request):
    # Process order
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data["form"]["total"])
    order.transaction_id = transaction_id

    # Mark order as complete if total matches cart total
    if total == order.get_cart_total:
        order.complete = True
    order.save()

    # Create shipping address if applicable
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
    # View product details
    product = Product.objects.filter(id=id).first()
    data = cartData(request)
    
    # Determine quantity of the product in the cart
    if request.user.is_authenticated:
        try:
            quantity = OrderItem.objects.filter(product=product).first().quantity
        except:
            quantity = 0
    else:
        quantity = 0
        try:
            for item in data["items"]:
                if item['product']['id'] == id:
                    quantity = item['quantity']
        except:
            pass
        
    cartItems = data["cartItems"]
    
    # Prepare context for rendering the product page
    context = {"product": product, "cartItems": cartItems, "title":"PRODUCT", "quantity": quantity}
    return render(request, "shop/product.html", context)

def about(request):
    # Render the about page
    data = cartData(request)
    cartItems = data["cartItems"]
    return render(request, "shop/about.html", {"title":"ABOUT", "cartItems": cartItems})

def category(request, category_name):
    # View products by category
    category = Category.objects.filter(category_name=category_name).first()
    products = Product.objects.filter(category=category).all()
    
    data = cartData(request)
    cartItems = data["cartItems"]
    
    # Prepare context for rendering the shop page with filtered products by category
    context = {
        "title": "CATEGORY",
        "range": range(5),
        "products": products,
        "category": category,
        "shipping": False,
        "cartItems": cartItems,
    }
    
    return render(request, "shop/shop.html", context)
