from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, MemberList, Member
from django.forms import ModelForm

class MembersForm(ModelForm):
    class Meta:
        model = MemberList
        fields = '__all__'

