from django.shortcuts import render, redirect
from shop.utilities import cartData
from .models import *
from.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


# View for displaying user profile
@login_required
def profile(request):
    # Fetch cart data for the user
    data = cartData(request)
    cartItems = data["cartItems"]
    # Get the user's profile
    profile_ = Profile.objects.filter(user=request.user).first()
    
    # Context for rendering the profile page
    context={
        'title':'PROFILE',
        'cartItems':cartItems,
        'profile': profile_,
        }
    
    # Check if the user has a profile and print the profile image URL
    if profile_ is not None:
        print(profile_.imageurl)
    
    # Render the profile page
    return render(request, "authentication/profile.html", context)  

# View for handling user login
def login_user(request):
    # Fetch cart data for the user
    data = cartData(request)
    cartItems = data["cartItems"]
    
    # If the request method is POST (form submission)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Log in user and redirect to the home page
                login(request, user)
                next_url = request.GET.get("next")
                if next_url:
                    return redirect(next_url)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    
    # Context for rendering the login page
    context={
        'title':'LOGIN',
        'cartItems':cartItems,
        'form':form
        }
    
    # Render the login page
    return render(request, "authentication/login.html", context)

# View for handling user signup
def signup_user(request):
    # Fetch cart data for the user
    data = cartData(request)
    cartItems = data["cartItems"]
    
    # If the request method is POST (form submission)
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            # Save user registration form
            form.save()
            user = User.objects.filter(username=request.POST.get("username")).first()
            # Create a corresponding customer profile
            Customer.objects.create(user=user,first_name=user.first_name,last_name=user.last_name, email=user.email)
            Profile.objects.create(user=user)
            return redirect("login")
    else:
        form = CustomerRegisterForm()
        
    # Context for rendering the user signup page
    context={
        'title':'SIGNUP',
        'cartItems':cartItems,
        'form':form
        }
    
    # Render the user signup page
    return render(request, "authentication/signup-user.html", context)    

# View for handling business signup
def signup_business(request):
    # Fetch cart data for the user
    data = cartData(request)
    cartItems = data["cartItems"]
    
    # If the request method is POST (form submission)
    if request.method == 'POST':
        customer_form = CustomerRegisterForm(request.POST)
        business_form = BusinessRegisterForm(request.POST)
        if customer_form.is_valid() and business_form.is_valid():
            # Save user registration forms
            customer_form.save()
            user = User.objects.filter(username=request.POST.get("username")).first()
            # Create a corresponding business profile
            Business.objects.create(owner=user,business_name=request.POST.get("business_name"),first_name=user.first_name,last_name=user.last_name, email=user.email)
            Profile.objects.create(user=user)
            return redirect("login")
    else:
        customer_form = CustomerRegisterForm()
        business_form = BusinessRegisterForm()
        
    # Context for rendering the business signup page
    context={
        'title':'SIGNUP',
        'cartItems':cartItems,
        'customer_form':customer_form,
        'business_form':business_form
        }
    
    # Render the business signup page
    return render(request, "authentication/signup-business.html", context)    

# View for handling user logout
def logout_u(request):
    # Log out the user and redirect to the home page
    logout(request)
    return redirect("home")

# View for rendering terms and conditions page
def terms_conditions(request):
    # Fetch cart data for the user
    data = cartData(request)
    cartItems = data["cartItems"]
    # Render the terms and conditions page
    return render(request, "authentication/terms_conditions.html", {'title':'TERMS & CONDITIONS', 'cartItems':cartItems})
