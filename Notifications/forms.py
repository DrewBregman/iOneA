from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notification
from main.models import uProjects
from projects.models import Project

class newUProj(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    project = forms.ModelChoiceField(queryset=Project.objects.all(),empty_label=None)
    class Meta:
        model = uProjects
        fields = ['user', 'project', 'title']

