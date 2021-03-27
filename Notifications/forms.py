from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notification
from projects.models import uProjects
from projects.models import Project

class newUProj(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(newUProj, self).__init__(*args, **kwargs)
        list = uProjects.objects.filter(user=self.user, ifAdmin = True, ifAccepted = True)
        #list3 = list.objects
        list1 = []
        for item in list:
            list1.append(item.project.id)
        self.fields['project'] = forms.ModelChoiceField(queryset=Project.objects.filter(id__in=list1),empty_label=None)
    #list1 = uProjects.objects(user = self.user)
    #for uProj in list:
     #   list1.append(uProj.project)
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    #project = forms.ModelChoiceField(queryset=list1,empty_label=None)
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Define their role'}))
    class Meta:
        model = uProjects
        fields = ['user', 'project', 'title','ifAdmin']



class acceptForm(forms.ModelForm):
    ifAccepted = forms.BooleanField()
    class Meta:
        model = uProjects
        fields = ['ifAccepted']

class allowForm(forms.ModelForm):
    ifAccepted = forms.BooleanField(required=False)
    ifAdmin = forms.BooleanField(required=False)
    title = forms.CharField(required=False)
    class Meta:
        model = uProjects
        fields = ['ifAccepted', 'title', 'ifAdmin']