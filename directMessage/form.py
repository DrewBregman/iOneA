from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message
from django.forms import ModelForm


class MessageForm(ModelForm):
    class Meta:
        model = MemberList
        model = Project
        fields=['sender', 'receiver','content','time_created']

#inbox
#Message.objects.filter(reciever=request.user)
#sentbox
#Message.objects.filter(sender = request.user)