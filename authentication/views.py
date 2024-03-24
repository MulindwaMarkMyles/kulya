from django.shortcuts import render
from shop.utilities import cartData
from .models import *
from django.contrib.auth.decorators import login_required

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

def login(request):

    return render(request, "shop/login.html")

def signup(request):
    
    return render(request, "shop/signup.html")    

