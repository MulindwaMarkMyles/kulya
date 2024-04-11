from django.shortcuts import render, redirect
from django.http import JsonResponse
from shop.utilities import cartData
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
import json, os

@login_required
def profile(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    profile_ = Profile.objects.filter(user=request.user).first()
    
    context={
        'title':'PROFILE',
        'cartItems':cartItems,
        'profile': profile_,
        }
    if profile_ is not None:
        print(profile_.imageurl)
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

def add_products(request, business_name):
    data = cartData(request)
    cartItems = data["cartItems"]
    
    if request.method == 'POST':
        form = BusinessAddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product = Product.objects.filter(name=request.POST.get("name"), price=request.POST.get("price"), description=request.POST.get("description"), category=request.POST.get("category")).first()
            old_image_name = product.imageurl
            product.owner = Business.objects.filter(business_name=business_name).first()
            product.save()
            os.rename("../"+old_image_name, "../"+product.imageurl)
            return redirect("shop")
    else:
        form = BusinessAddProductsForm()
        
    context={
        'title':'ADD PRODUCTS',
        'cartItems':cartItems,
        'form':form
        }
    return render(request, "authentication/add-products.html", context)