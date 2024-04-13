from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from shop.models import *

class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)  # Username field
    password = forms.CharField(required=True, widget=forms.PasswordInput)  # Password field

    class Meta:
        model = User  # Django User model
        fields = ["username", "password"]  # Form fields

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        # Add CSS classes to form fields
        self.fields["username"].widget.attrs['class'] = 'login-form-field'
        self.fields["password"].widget.attrs['class'] = 'login-form-field'

class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Email field
    first_name = forms.CharField(required=True)  # First name field
    last_name = forms.CharField(required=True)  # Last name field

    class Meta:
        model = User  # Django User model
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']  # Form fields

    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm, self).__init__(*args, **kwargs)
        # Add CSS classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'login-form-field'

class BusinessRegisterForm(forms.Form):
    business_name = forms.CharField(required=True)  # Business name field

    class Meta:
        model = Business  # Business model
        fields = ['business_name']  # Form fields

    def __init__(self, *args, **kwargs):
        super(BusinessRegisterForm, self).__init__(*args, **kwargs)
        # Add CSS class to form field
        self.fields["business_name"].widget.attrs['class'] = 'login-form-field'
        
class BusinessAddProductsForm(forms.ModelForm):
    name = forms.CharField(required=True)  # Product name field
    price = forms.DecimalField(required=True)  # Product price field
    description = forms.TextInput()  # Product description field
    image = forms.ImageField(required=True)  # Product image field
    digital = forms.CheckboxInput()  # Digital product field
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)  # Product category field

    class Meta:
        model = Product  # Product model
        fields = ['name', 'price', 'description', 'image', 'digital', 'category']  # Form fields

    def __init__(self, *args, **kwargs):
        super(BusinessAddProductsForm, self).__init__(*args, **kwargs)
        # Add CSS classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'add-form-field'
        self.fields['description'].widget.attrs['required'] = True





