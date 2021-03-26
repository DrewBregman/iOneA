from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, MemberList, Member
from django.forms import ModelForm

class MembersForm(ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Member
        fields = ['username', 'is_admin']

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['name', 'department', 'department','bPic', 'logo',
        'description', 'purpose', 'projectTag', 'lookingFor', 'recruiting']
class CreateForm(ModelForm):
    class Meta:
        model = MemberList
        model = Project
        fields=['name', 'department', 'department','bPic', 'logo',
        'department', 'purpose', 'projectTag', 'lookingFor', 'recruiting']
