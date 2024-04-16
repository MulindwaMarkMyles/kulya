from django.shortcuts import render, redirect
from django.http import JsonResponse
from shop.utilities import cartData
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
import json
from django.contrib import messages

@login_required
def profile(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    business_owner = ""

    try:
        the_user = Customer.objects.filter(user=request.user).first()
        if len(Customer.objects.filter(user=request.user)) == 0:
            raise ValueError
        orders = Order.objects.filter(customer=request.user).order_by("-date_ordered")
        the_user = "bustomer"

    except Exception as e:
        the_user = "Business"
        business = Business.objects.filter(owner=request.user).first()
        orderitems = OrderItem.objects.filter(product__owner=business).order_by("-date_added")
        orders = []
        for orderitem in orderitems:
            orders.append(orderitem.order)
        print(orders)
        business_owner = business
        
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            customer = Customer.objects.filter(user=request.user).first()
            customer.first_name = f"{user_form.cleaned_data.get('first_name')}"
            customer.last_name = f"{user_form.cleaned_data.get('last_name')}"
            customer.email = f"{user_form.cleaned_data.get('email')}"
            
            customer.save()
            return redirect("profile")
            
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

    real_list = []
    for order in orders:
        if order.transaction_id:
            real_list.append(order)
    
    context={
        'title':'PROFILE',
        'cartItems':cartItems,
        'profile_form': profile_form,
        'user_form': user_form,
        'orders': real_list,
        'the_user': the_user, 
        'business_owner': business_owner
        }
    
    return render(request, "authentication/profile.html",context)  

def login_user(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                next_url = request.GET.get("next")
                if next_url:
                    return redirect(next_url)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
            
    context={
        'title':'LOGIN',
        'cartItems':cartItems,
        'form':form
        }
            
    return render(request, "authentication/login.html", context)

def signup_user(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.filter(username=request.POST.get("username")).first()
            Customer.objects.create(user=user,first_name=user.first_name,last_name=user.last_name, email=user.email)
            Profile.objects.create(user=user)
            return redirect("login")
    else:
        form = CustomerRegisterForm()
        
    context={
        'title':'SIGNUP',
        'cartItems':cartItems,
        'form':form
        }
    return render(request, "authentication/signup-user.html", context)    

def signup_business(request):
    try:
        signup_data = json.loads(request.body)
    except:
        signup_data = {}
    data = cartData(request)
    cartItems = data["cartItems"]
    
    if signup_data:
        customer_form = CustomerRegisterForm(signup_data['form'])
        business_form = BusinessRegisterForm(signup_data['form'])
        if customer_form.is_valid() and business_form.is_valid():
            customer_form.save()
            user  = User.objects.filter(username=signup_data['form'].get("username")).first()
            Business.objects.create(owner=user,business_name=signup_data['form'].get("business_name"),first_name=user.first_name,last_name=user.last_name, email=user.email)
            Profile.objects.create(user=user)
            return JsonResponse("Business was created..", safe=False)
        else:
            messages.error(request, "There was an issue with those details, if you followed all instructions then that company is already registered.")
            return JsonResponse("Business was not created..", safe=False)
    else:
        customer_form = CustomerRegisterForm()
        business_form = BusinessRegisterForm()
        
    context={
        'title':'SIGNUP',
        'cartItems':cartItems,
        'customer_form':customer_form,
        'business_form':business_form
        }
    return render(request, "authentication/signup-business.html", context)    

def logout_u(request):
    logout(request)
    return redirect("home")

@login_required
def add_products(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    
    if request.method == 'POST':
        form = BusinessAddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product = Product.objects.filter(name=request.POST.get("name"), price=request.POST.get("price"), description=request.POST.get("description"), category=request.POST.get("category")).first()
            business = Business.objects.filter(owner=request.user).first()
            product.owner = business
            product.save()
            return redirect("shop")
    else:
        form = BusinessAddProductsForm()
        
    context={
        'title':'ADD PRODUCTS',
        'cartItems':cartItems,
        'form':form
        }
    return render(request, "authentication/add-products.html", context)