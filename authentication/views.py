from django.shortcuts import render,redirect
from .models import Customer, Business
from django.urls import reverse
from django.contrib.auth import authenticate, login


def customer_signup(request):
        if request.method == 'POST':
             first_name = request.POST.get('first_name')
             last_name = request.POST.get('last_name')
             email = request.POST.get('email')
             password = request.POST.get('password')
             new_customer = Customer.objects.create(first_name=first_name, last_name=last_name,email=email,password=password)
             new_customer.save()
             return redirect(reverse('login'))
        else:
             return render(request,'authentication/customer_signup.html')
        
def business_signup(request):
    if request.method == 'POST':
             first_name = request.POST.get('first_name')
             last_name = request.POST.get('last_name')
             business_name = request.POST.get('business_name')
             email = request.POST.get('email')
             password = request.POST.get('password')
             new_business = Business.objects.create(first_name=first_name, last_name=last_name,business_name=business_name, email=email,password=password)
             new_business.save()
             return redirect(reverse('login'))
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
                   return redirect(reverse('product'))
             else:
            # Return an invalid login message
                   return render(request, 'authentication/login.html', {'error_message': 'Invalid email or password'})
        return render(request, 'authentication/login.html')
                   