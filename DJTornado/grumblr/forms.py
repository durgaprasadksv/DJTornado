from django import forms

from django.contrib.auth.models import User
from models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class CreateUserForm(forms.Form):

    username = forms.CharField(max_length = 20, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder':'Username'}))
    email = forms.CharField(max_length=20, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder':'Email'}))
    first_name = forms.CharField(max_length = 200, 
                                label='first name',
                                widget=forms.TextInput(attrs={'class': 'form-control input-lg', 
                                    'placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 200, 
                              label='last name',
                              widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder':'Last Name'}))
    password1 = forms.CharField(max_length = 200, 
                                label='Password', required = True,
                                 widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder':'Password','type':'password'}))
    password2 = forms.CharField(max_length = 200, 
                                label='Confirm password', required=True,  
                                 widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder':'Confirm Password','type':'password'}))


    def clean(self):

        cleaned_data = super(CreateUserForm, self).clean()
        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # Generally return the cleaned data we got from our parent.
        return cleaned_data

    # username should be unique
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__exact=email):
            raise forms.ValidationError('Email already registered. ')
        return email

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'Username', 
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder':'Password', 
    }))
