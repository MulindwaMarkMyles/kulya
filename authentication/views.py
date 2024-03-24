from django.shortcuts import render, redirect
from shop.utilities import cartData
from .models import *
from.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

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
    print(profile_.imageurl)
    return render(request, "auth/profile.html",context)  

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
            
    return render(request, "auth/login.html", context)

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
    return render(request, "auth/signup-user.html", context)    

def signup_business(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    
    if request.method == 'POST':
        customer_form = CustomerRegisterForm(request.POST)
        business_form = BusinessRegisterForm(request.POST)
        if customer_form.is_valid() and business_form.is_valid():
            customer_form.save()
            user = User.objects.filter(username=request.POST.get("username")).first()
            Business.objects.create(user=user,business_name=request.POST.get("business_name"),first_name=user.first_name,last_name=user.last_name, email=user.email)
            Profile.objects.create(user=user)
            return redirect("login")
    else:
        customer_form = CustomerRegisterForm()
        business_form = BusinessRegisterForm()
        
    context={
        'title':'SIGNUP',
        'cartItems':cartItems,
        'customer_form':customer_form,
        'business_form':business_form
        }
    return render(request, "auth/signup-business.html", context)    

