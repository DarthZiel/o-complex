from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")



