from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Notification
from django.db.models import Q
from .forms import newUProj, acceptForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from main.models import uProjects
from django.contrib.auth.models import User
from projects.models import Project

class SearchResultsView(ListView):
    model = Notification
    template_name = 'noti.html'

    def get_queryset(self):
        return Notification.objects.filter(user = self.request.user)

def invite(request):
    if request.method == "POST":
        form = newUProj(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            data = form.cleaned_data.get("user")
            data1 = form.cleaned_data.get('project')
            #messages.success(request, f'Your account has been updated!')
            n = Notification(user = data, message = "You have a new project request. " + request.user.username + ' wants you to join ' + str(data1) + '.',
                             url = 'http://127.0.0.1:8000/accept/' + str(data) + '/' + str(data1))
            n.save()
            return redirect('/')
    else:
        form = newUProj(request.POST, user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'invite.html', context)
# Create your views here.
@login_required
def accept(request, name1, name2):
    user = User.objects.get(username=name1)
    project = Project.objects.get(name=name2)
    if uProjects.objects.filter(user = user, project = project).exists():
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
        }
        return render(request, 'accept.html', context)
    return redirect('/')
