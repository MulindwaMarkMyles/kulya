from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utilities import *
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view

#Shop view using a rest api
class ShopView(APIView):
    #get method to retrieve all products
    def get(self, request):
        # Retrieve cart data
        data = cartData(request)
        cartItems = data["cartItems"]
        
        # Retrieve all products
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

    #post method to handle search functionality
    def post(self, request):
        # Retrieve cart data
        data = cartData(request)
        cartItems = data["cartItems"]
        
        # Handle search functionality
        searchterm = request.data.get("searchterm")
        products = Product.objects.filter(name__contains=searchterm)

        # Prepare context for rendering the shop page
        context = {
            "title": "SHOP",
            "range": range(5),
            "products": products,
            "cartItems": cartItems,
            "shipping": False,
        }
        return render(request, "shop/shop.html", context)

@api_view(['GET'])
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


@api_view(['GET'])
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

@login_required
def checkout(request):
    # Retrieve cart data
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    if request.method == 'POST':
        shipping_form = ShippingAddressForm(request.POST)
        if shipping_form.is_valid():
            shipping_form.save()
            shippingaddress = ShippingAddress.objects.filter(
                address=shipping_form.cleaned_data['address'], 
                city=shipping_form.cleaned_data['city'],
                state=shipping_form.cleaned_data['state'],
                zipcode=shipping_form.cleaned_data['zipcode'],
                ).first()
            customer = request.user
            transaction_id = datetime.datetime.now().timestamp()
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            order.transaction_id = transaction_id
            shippingaddress.customer = customer
            shippingaddress.order = order
            order.save()
            shippingaddress.save()
            
            
            return redirect("process-order")
    else:
        shipping_form = ShippingAddressForm()
        user_form = UserInfoForm(initial={
            "first_name":request.user.first_name, 
            "last_name":request.user.last_name, 
            "email":request.user.email})
    # Prepare context for rendering the checkout page
    context = {
        "title": "CHECKOUT",
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "shipping_form": shipping_form,
        "user_form": user_form
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
    
    data = cartData(request)
    cartItems = data["cartItems"]
    
    host = request.get_host()
    order = Order.objects.filter(customer=request.user).first()
    total = order.get_cart_total

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.transaction_id),
        'currency_code': 'USD',
        'notify_url': f'https://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("payment-success")}',
        'cancel_url': f'http://{host}{reverse("payment-failure")}',
    }
    
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    context = {"paypal": paypal_payment, "cartItems": cartItems, "title":"PAYMENT"}
    
    return render(request, "shop/payment.html", context)

@api_view(['GET'])
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

@api_view(['GET'])
def about(request):
    # Render the about page
    data = cartData(request)
    cartItems = data["cartItems"]
    return render(request, "shop/about.html", {"title":"ABOUT", "cartItems": cartItems})

@api_view(['GET'])
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

def paymentsuccessful(request):
    # Render the payment successful page
    data = cartData(request)
    cartItems = data["cartItems"]
    return render(request, "shop/paymentsuccessful.html", {"title":"PAYMENT SUCCESSFUL", "cartItems": cartItems})

def paymentfailed(request):
    # Render the payment failed page
    data = cartData(request)
    cartItems = data["cartItems"]
    return render(request, "shop/paymentfailed.html", {"title":"PAYMENT FAILED", "cartItems": cartItems})