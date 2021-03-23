from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Project
from users.models import Profile
from django.db.models import Q
from .forms import MembersForm, CreateForm, ProjectUpdateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import uProjects
from django.contrib.auth.decorators import user_passes_test
from functools import wraps


def SearchResultsView(request):

    query=request.GET.get('q')
    object_list=Project.objects.filter(
    Q(name__icontains=query) | Q(projectTag__icontains=query))
    object_list1=Project.objects.filter(Q(department__icontains=query))
    profilelist1 = Profile.objects.filter(Q(firstName =query) | Q(interest=query))
    final_list = list(set(object_list) | set(object_list1))
    profile_list = list(set(profilelist1))
    context = {
        'object_list': final_list,
        'profile_list': profile_list

    }
    return render(request, 'search_results.html', context)

class SearchPageView(TemplateView):
    template_name = 'searchbar.html'

def createProject(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            n = uProjects(user = request.user, project = Project.objects.get(name = form.cleaned_data.get('name'), purpose = form.cleaned_data.get('purpose')), ifAdmin = True, ifAccepted = True)
            n.save()
        #return render(request, 'projects/projectpage.html')
        return redirect('/project/' + form.cleaned_data.get('name'))
    else:
        form = CreateForm()
    return render(request, 'projects/createProject.html', {'form': form})

#update projects
@login_required
def project(request, name):

    #return render(request, 'projects/projectpage.html')
    project = Project.objects.get(name= name)

    j = True
    if uProjects.objects.filter(project = Project.objects.get(name = name), user = request.user):
        j = False
    url = '/editproject/' + name
    context = {
        "pp": project,
        "projurl": url,
        'boo':j
    }
    return render(request, 'projects/projectpage.html', context)


def admin_check(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        user = request.user
        name = kwargs.get('name')  
        if uProjects.objects.filter(project=Project.objects.get(name=name), user=user, ifAdmin=True).exists():
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
  return wrap

@admin_check
def update(request, name):
    project = Project.objects.get(name = name)
    if request.method == "POST":
        pr_form = ProjectUpdateForm(request.POST,
                                    request.FILES,
                                    instance=project)
    #if is_admin in Member == True: #need to authenticate user, access user permissions, if user has permission:
        if pr_form.is_valid():
            pr_form.save()
            messages.success(request, f'This project has been updated.')
            return redirect('project')
        
    else:
        pr_form = ProjectUpdateForm(instance=project)
    context = {
        'pr_form': pr_form
    }
    return render(request, 'projects/updateproject.html', context)
