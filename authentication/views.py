from django.shortcuts import render,redirect
from .models import Customer, Business
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

def customer_signup(request):
        if request.method == 'POST':
             first_name = request.POST.get('first_name')
             last_name = request.POST.get('last_name')
             email = request.POST.get('email')
             password = request.POST.get('password')
             new_customer = Customer.objects.create(first_name=first_name, last_name=last_name,email=email,password=password)
             new_customer.save()
             return redirect('login')
        else:
             return render(request,'authentication/customer_signup.html')
        
def business_signup(request):
    if request.method == 'POST':
             first_name = request.POST.get('first_name')
             last_name = request.POST.get('last_name')
             business_name = request.POST.get('business_name')
             email = request.POST.get('email')
             password = request.POST.get('password')
             password_confirm = request.POST.get('password_confirm')
             # Check if the passwords match
             if password != password_confirm:
                 return render(request, "authentication/business_signup.html", {'error': 'Passwords do not match'})
             hashed_password = make_password(password)
             new_business = Business.objects.create(first_name=first_name, last_name=last_name,business_name=business_name, email=email,password=hashed_password)
             new_business.save()
             return redirect('login')
    else:
          return render(request, "authentication/business_signup.html")

def login(request):
        if request.method == 'POST':
             email = request.POST.get('email')
             password = request.POST.get('password')
             #check for account
             customer = authenticate(email=email, password=password)
             if customer is not None:
                   login(request,customer)
                   return redirect('product')
             else:
            # Return an invalid login message
                   return render(request, 'authentication/login.html', {'error_message': 'Invalid email or password'})
        return render(request, 'authentication/login.html')
                   
def Sign_Up(request):
      if request.method == 'POST':
            account_type = request.POST.get("account_type")
            if account_type == "customer":
                  return redirect('customer_signup')
            elif account_type == 'business':
                     return redirect('business_signup')
      return render(request, 'authentication/Sign_Up.html')    
        
def profile(request):
      return HttpResponse('profile')