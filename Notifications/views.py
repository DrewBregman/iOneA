from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Notification
from django.db.models import Q
from .forms import newUProj, acceptForm, allowForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from projects.models import Project, uProjects

@login_required()
def Notifications(request):
    noti = Notification.objects.filter(user = request.user)
    project = Project.objects.all()
    context = {
        'object_list': noti,
        'project_list': project

    }
    noti1 = Notification.objects.filter(ifViewed = False)
    for object in noti1:
        object.ifViewed = True
        object.save()
    return render(request, 'noti.html', context)

def invite(request):
    if request.method == "POST":
        form = newUProj(request.POST,user=request.user)
        if form.is_valid():
            data = form.cleaned_data.get("user")
            data1 = form.cleaned_data.get('project')
            data2 = data1.id
            #messages.success(request, f'Your account has been updated!')
            n = Notification(user = data, message = "You have a new project request. " + request.user.username + ' wants you to join ' + str(data1) + '.',
                             url = 'http://127.0.0.1:8000/accept/' + str(data) + '/' + str(data2))
            if uProjects.objects.filter(user = data, project = data1).exists():
                pass
            else:
                n.save()
                form.save()
            return redirect('/')
    else:
        form = newUProj(request.POST, user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'invite.html', context)
# Create your views here.
@login_required
def accept(request, name1, id):
    user = User.objects.get(username=name1)
    project = Project.objects.get(id = id)
    if uProjects.objects.filter(user = user, project = project).exists() and user == request.user:
        context = {
            "user": user,
            "project": project
        }
        #return render(request, 'accept.html', {'u': user, 'p': project})
        if request.method == "POST":
            form = acceptForm(request.POST)
            if form.is_valid():
                #form.save()
                data = form.cleaned_data.get("ifAccepted")
                #messages.success(request, f'Your account has been updated!')
                #n = Notification(user = data, message = "You have a new project request. " + request.user.username + ' wants you to join ' + str(data1) + '.',
                 #                url = 'http://127.0.0.1:8000/agree/' + str(data) + '/' + str(data1))
                if data == True:
                    n = uProjects.objects.get(user = user, project = project, ifAccepted = False)
                    n.ifAccepted = True
                    n.save()
                else:
                    n = uProjects.object.get(user=user, project=project)
                    n.delete()
                return redirect('/')
        else:
            form = acceptForm(request.POST)
        context = {
            'form': form,
            'projname': project.name
        }
        return render(request, 'accept.html', context)
    return redirect('/')
@login_required
def allow(request, name1, id):
    user = User.objects.get(username=name1)
    project = Project.objects.get(id = id)
    if uProjects.objects.filter(user = request.user, project = project, ifAdmin = True, ifAccepted = True).exists():
        context = {
            "user": user,
            "project": project
        }
        #return render(request, 'accept.html', {'u': user, 'p': project})
        if request.method == "POST":
            form = allowForm(request.POST)
            if form.is_valid():
                #form.save()
                data = form.cleaned_data.get("ifAccepted")
                data1 = form.cleaned_data.get('title')
                data2 = form.cleaned_data.get('ifAdmin')
                #messages.success(request, f'Your account has been updated!')
                #n = Notification(user = data, message = "You have a new project request. " + request.user.username + ' wants you to join ' + str(data1) + '.',
                 #                url = 'http://127.0.0.1:8000/agree/' + str(data) + '/' + str(data1))
                if data == True:
                    n = uProjects.objects.get(user = user, project = project)
                    n.ifAccepted = True
                    n.title = data1
                    n.ifAdmin = data2
                    n.save()
                else:
                    n = uProjects.object.get(user=user, project=project)
                    n.delete()
                return redirect('/')
        else:
            form = allowForm(request.POST)
        context = {
            'form': form,
            'projname': project.name,
            'user' : user.username,
        }
        return render(request, 'allow.html', context)
    return redirect('/')

def request(request, name, id):
    if uProjects.objects.filter(user=request.user, project=Project.objects.get(id = id)).exists():
        pass
    else:
        j = uProjects(user=request.user, project=Project.objects.get(id = id), ifAccepted=False)
        j.save()
        admins = uProjects.objects.filter(project = Project.objects.get(id = id), ifAccepted = True, ifAdmin = True)
        for object in admins:
            n = Notification(user=object.user,
                             message="You have a new project request. " + request.user.username + ' wants to join ' + str(
                                 object.project.name) + '.',
                             url='http://127.0.0.1:8000/allow/' + str(request.user.username) + '/' + str(object.project.id))
            n.save()
    return redirect('/profile')