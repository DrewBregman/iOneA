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
from .models import uProjects
from django.contrib.auth.decorators import user_passes_test
from functools import wraps


def SearchResultsView(request):
    query=request.GET.get('q')
    searchQuery=request.GET.get('z')
    project_list = []
    profile_list= []
    udepartment_list=[]
    pdepartment_list=[]

    if searchQuery == "searchUser":
        profile_list1 = Profile.objects.filter(Q(firstName__icontains =query) | Q(interest__icontains=query))
        profile_list2 = Profile.objects.filter(Q(lastName__icontains =query) | Q(company__icontains=query) | Q(Department__icontains=query))
    
        profile_list = list(set(profile_list1) | set(profile_list2))
        
    elif searchQuery == "searchProject":
        project_list1=Project.objects.filter(
                                            Q(name__icontains=query) | Q(projectTag__icontains=query))
        project_list2=Project.objects.filter(Q(department__icontains=query) | Q(lookingFor__icontains=query))
    
        project_list = list(set(project_list1) | set(project_list2))
    elif searchQuery == "searchDepartment":
        #return HttpResponse('Sorry, this feature is currently unavailable, please search by User or Project.')
        pdepartment_list=Project.objects.filter(Q(department__icontains=query))
        udepartment_list=Profile.objects.filter(Q(Department__icontains=query))
        udepartment_list = list(set(udepartment_list))
        pdepartment_list = list(set(pdepartment_list))
    elif searchQuery == "searchFaculty":
        return HttpResponse('Sorry, this feature is currently unavailable, please search by User.')
    else: 
        return HttpResponse('Sorry, please make a search by selection and try again.')
        
   
    context = {
        'project_list': project_list,
        'profile_list': profile_list,
        'udepartment_list': udepartment_list,
        'pdepartment_list': pdepartment_list,
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
    if uProjects.objects.filter(project = Project.objects.get(name = name), user = request.user) or project.recruiting == False:
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
            instance= pr_form.save()
            pr_form.save()
            messages.success(request, f'This project has been updated.')
           
        
            return redirect('project', name=instance.name)
        
    else:
        pr_form = ProjectUpdateForm(instance=project)
    context = {
        'pr_form': pr_form
    }
    return render(request, 'projects/updateproject.html', context)


@login_required
def myProjects(request):
    user = request.user
    object_list=uProjects.objects.filter(user=user) 
    context = {
        'object_list': object_list,
    }
    return render(request, 'projects/myprojects.html', context)

