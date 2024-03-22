import json
from .models import *
from authentication.models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES["cart"])
    except:
        cart = {}

    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0}
    cartItems = order["get_cart_items"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            product = Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]
            order["get_cart_items"] += cart[i]["quantity"]
            order["get_cart_total"] += total

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageurl": product.imageurl,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }

            items.append(item)
            if product.digital == False:
                order["shipping"] = True
        except:
            pass
    return {"cartItems": cartItems, "items": items, "order": order}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
        if order == None:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData["cartItems"]
        order = cookieData["order"]
        items = cookieData["items"]

    return {"cartItems": cartItems, "items": items, "order": order}


def guestOrder(request, data):
    first_name = data["form"]["first_name"]
    last_name = data["form"]["last_name"]
    email = data["form"]["email"]

    cookieData = cookieCart(request)
    items = cookieData["items"]

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.first_name = first_name
    customer.last_name = last_name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item["product"]["id"])
        orderItems = OrderItem.objects.create(
            product=product, order=order, quantity=item["quantity"]
        )
    return customer, order

