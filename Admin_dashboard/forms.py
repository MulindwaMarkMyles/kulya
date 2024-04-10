from django import forms
from django.contrib.auth.models import User
from authentication.models import Profile,Business,Customer

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['first_name', 'last_name', 'business_name', 'email']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image']




