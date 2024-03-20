from django.shortcuts import render
from shop.views import *

<<<<<<< HEAD
# Create your views here.
def profile(request):
    context={
        'title':'Uer Profile',
        'name':'USER NAME',
        'email':'USER EMAIL',
        'phone_number':'PHONE NUMBER'
         }

    return render(request, "shop/login.html",context)  

def login(request):

    return render(request, "shop/profile.html") 
=======
# Create your views here.
>>>>>>> df37b3c8285b5ff32c46c058c956a0c36cc59067
