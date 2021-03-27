from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from phonenumber_field.modelfields import PhoneNumberField

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
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    #email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    Major = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'What is your major?'}))
    Minor = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Do you have a minor?'}))
    interest = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Your academic or commmercial interests are..."}))
    expertise = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"You have expertise in..."}))
    research_goals = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Your research goals are..."}))
    interest = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Your academic or commmercial interests are..."}))
    expertise = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"You have expertise in..."}))
    research_goals = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Your research goals are..."}))
    phone = PhoneNumberField()
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'Major', 'Minor', 'title', 'gradYear',
                'company', 'phone', 'Department', 'interest', 'expertise', 'research_goals',
                'lookingFor', 'image', 'twitter']
class infoForm(forms.Form):

    class Meta:
        model = Profile
        fields = ["firstName","lastName","image","email","Department"]
