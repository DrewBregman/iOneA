from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, infoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #j = Profile(user = User.objects.get(username = username))
            #j.save()
            return redirect('login')
        #messages.success(request, 'Your account has been created! You are now able to log in')
        #return HttpResponse("regii")
    form = RegisterForm()
    return render(request, "users/register.html", {'form':form})

def home(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            request.user.profile.first = False
            request.user.profile.save()
            return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            context = {
                'u_form': u_form,
                'p_form': p_form
            }
            first = request.user.profile.first
            if first == True:
                request.user.profile.save()
                return render(request, 'users/updateprofile.html', context)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        first = request.user.profile.first
        if first == True:
            request.user.profile.save()
            return render(request, 'users/updateprofile.html', context)
    return redirect('/')

@login_required
def profile(request, id):
    profile = Profile.objects.get(id= id)
    user = profile.user
    context = {
        "profile": profile
    }
    return render(request, 'users/profile1.html', {'dj': user})

@login_required
def profile1(request):
    profile = request.user.profile
    user = profile.user
    context = {
        "profile": profile
    }
    return render(request, 'users/profile.html', {'dj': user})

@login_required
def updateprofile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/updateprofile.html', context)