# store/forms.py
from django import forms
from .models import Product
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']