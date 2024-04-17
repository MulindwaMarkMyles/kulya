from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    
    class Meta:
        model = ShippingAddress
        fields = ["address", "city", "state", "zipcode"]
        
    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
class UserInfoForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control'}))
    
    
    