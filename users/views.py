from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, infoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(response, f'Account {username} has been created! You are now able to log in')
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(response, "users/register.html", {'form':form})

def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account updated!!!')
            request.user.profile.first = False
            return redirect('/Create')
    else:
        form = infoForm()
        first = request.user.profile.first
        if first == True:
            request.user.profile.save()
            return render(request, "users/info.html", {'form':form})
        return redirect('/')

@login_required
def profile(request):
    return render(request, 'users/profile.html')