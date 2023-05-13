from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Message

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Body'}))


    class Meta:
        model = Message
        fields = ['recipient', 'name', 'email', 'subject', 'body']