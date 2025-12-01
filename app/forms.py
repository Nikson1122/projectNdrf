from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Product, ContactMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields =('username', 'email', 'is_app_admin')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_app_admin')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class BuyProductForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    product_name = forms.CharField(
        label="Product Name",
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    product_price = forms.DecimalField(
        label="Price",
        widget=forms.NumberInput(attrs={'readonly': 'readonly'})
    )
    quantity = forms.IntegerField(label="Quantity", min_value=1)
    customer_name = forms.CharField(label="Your Name", max_length=255)
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(label="Phone Number", max_length=20)



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

