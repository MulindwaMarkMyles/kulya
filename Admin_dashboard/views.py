from django.shortcuts import render,redirect,get_object_or_404
from authentication.models import Business, Customer, Profile
from .forms import *


def page(request):
    """Renders the custom admin login page."""
    return render(request, "Admin_dashboard/customadminlogin.html")

def admin_page(request):
    """Renders the admin dashboard page."""
    return render(request, "Admin_dashboard/admin_page.html")

def business_list(request):
    """Renders a list of all businesses."""
    businesses = Business.objects.all()
    return render(request, "Admin_dashboard/business_list.html", {'businesses': businesses})

def business_detail(request, pk):
    """Renders the details of a specific business."""
    business = get_object_or_404(Business, pk=pk)
    return render(request, 'business_detail.html', {'business': business})

def business_create(request):
    """Handles the creation of a new business."""
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm()
    return render(request, 'Admin_dashboard/business_create.html', {'form': form})

def business_delete(request, pk):
    """Handles the deletion of a business."""
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        business.delete()
        return redirect('business_list')
    return render(request, 'Admin_dashboard/business_delete.html', {'business': business})

def customer_list(request):
    """Renders a list of all customers."""
    customers = Customer.objects.all()
    return render(request, "Admin_dashboard/customer_list.html", {'customers': customers})

def customer_detail(request, pk):
    """Renders the details of a specific customer."""
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_create(request):
    """Handles the creation of a new customer."""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'Admin_dashboard/customer_create.html', {'form': form})

def customer_delete(request, pk):
    """Handles the deletion of a customer."""
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'Admin_dashboard/customer_delete.html', {'customer': customer})

def profile_list(request):
    """Renders a list of all profiles."""
    profiles = Profile.objects.all()
    return render(request, "Admin_dashboard/profile_list.html", {'profiles': profiles})

def profile_detail(request, pk):
    """Renders the details of a specific profile."""
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile_detail.html', {'profile': profile})

def profile_create(request):
    """Handles the creation of a new profile."""
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'Admin_dashboard/profile_create.html', {'form': form})

def profile_delete(request, pk):
    """Handles the deletion of a profile."""
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'Admin_dashboard/profile_delete.html', {'profile': profile})


def index(request):
    return render(request,"Admin_dashboard/customadminlogin.html")

def adminpage(request):
    return render(request,"Admin_dashboard/adminpage.html")
