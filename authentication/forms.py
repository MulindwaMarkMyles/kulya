from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =["username", "password"]
        
    def __init__(self, *args, **kwargs):
        super(UserLoginForm,self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'login-form-field'
        self.fields["password"].widget.attrs['class'] = 'login-form-field'
        
class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required= True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm,self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'login-form-field'
            
class BusinessRegisterForm(forms.Form):
    business_name = forms.CharField(required=True)
    class Meta:
        model = Business
        fields = ['business_name']
        
    def __init__(self, *args, **kwargs):
        super(BusinessRegisterForm, self).__init__(*args, **kwargs)
        self.fields["business_name"].widget.attrs['class'] = 'login-form-field'
    