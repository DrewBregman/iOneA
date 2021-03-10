from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['firstName', 'lastName', 'Major', 'Minor', 'title', 'gradYear',
                'company', 'phone', 'Department', 'interest', 'expertise', 'research_goals',
                'lookingFor', 'image', 'twitter']
class infoForm(forms.Form):

    class Meta:
        model = Profile
        fields = ["firstName","lastName","image","email","Department"]
