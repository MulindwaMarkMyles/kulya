from django.shortcuts import render,redirect,get_object_or_404
from authentication.models import Business, Customer, Profile
from .forms import *

def page(request):
    return render(request, "Admin_dashboard/customadminlogin.html")

def admin_page(request):
    return render(request, "Admin_dashboard/admin_page.html")

def business_list(request):
    businesses = Business.objects.all()
    return render(request, "Admin_dashboard/business_list.html", {'businesses': businesses})

def business_detail(request, pk):
    business = get_object_or_404(Business, pk=pk)
    return render(request, 'Admin_dashboard/business_list.html', {'business': business})

def business_create(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm()
    return render(request, 'Admin_dashboard/business_create.html', {'form': form})

def business_delete(request, pk):
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        business.delete()
        return redirect('business_list')
    return render(request, 'Admin_dashboard/business_delete.html', {'businesses': business})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "Admin_dashboard/customer_list.html", {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'Admin_dashboard/customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'Admin_dashboard/customer_create.html', {'form': form})

def customer_delete(request, pk):
    customers = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customers.delete()
        return redirect('customer_list')
    return render(request, 'Admin_dashboard/customer_delete.html', {'customers': customers})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "Admin_dashboard/profile_list.html", {'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile_detail.html', {'profile': profile})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'Admin_dashboard/customer_create.html', {'form': form})

def customer_delete(request, pk):
    customers = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customers.delete()
        return redirect('profile_list')
    return render(request, 'Admin_dashboard/customer_delete.html', {'customers': customers})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "Admin_dashboard/customer_list.html", {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'Admin_dashboard/customer_create.html', {'form': form})

def customer_delete(request, pk):
    customers = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customers.delete()
        return redirect('customer_list')
    return render(request, 'Admin_dashboard/customer_delete.html', {'customers': customers})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "Admin_dashboard/profile_list.html", {'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile_detail.html', {'profile': profile})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'Admin_dashboard/profile_create.html', {'form': form})

def profile_delete(request, pk):
    profiles = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profiles.delete()
        return redirect('profile_list')
    return render(request, 'Admin_dashboard/profile_delete.html', {'profiles': profiles})

def view_owner(request):
    business = Business.objects.all()
    return render(request, 'Admin_dashboard/view_owner.html')
