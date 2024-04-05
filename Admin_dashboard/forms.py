from django import forms
from django.contrib.auth.models import User
from authentication.models import Profile,Business,Customer

# Define BusinessForm to handle business-related form data
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business  # Associate the form with the Business model
        fields = ['first_name', 'last_name', 'business_name', 'email']  # Specify fields to include in the form

# Define CustomerForm to handle customer-related form data
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer  # Associate the form with the Customer model
        fields = ['first_name', 'last_name', 'email']  # Specify fields to include in the form

# Define ProfileForm to handle profile-related form data
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Associate the form with the Profile model
        fields = ['user', 'image']  # Specify fields to include in the form





