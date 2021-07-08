from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Project
from users.models import Profile
from django.db.models import Q
from .forms import MembersForm, CreateForm, ProjectUpdateForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import uProjects


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

    context = {
        "project": project
    }
    return render(request, 'projects/projectpage.html', {'pp': project, 'boo':j})

def update(request):
    if request.method == "POST":
        m_form = MembersForm(request.POST, instance=request.members)
        pr_form = ProjectUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.name)
    #if is_admin in Member == True: #need to authenticate user, access user permissions, if user has permission:
        if m_form.is_valid() and pr_form.is_valid():
            m_form.save()
            pr_form.save()
            messages.success(request, f'This project has been updated.')
            request.name.save()
            return redirect('project')
        else:
            m_form = MembersForm(instance=request.members)
            pr_form = ProjectUpdateForm(instance=request.name)
            context = {
                'm_form': m_form,
                'pr_form': pr_form,
            }

        return render(request, 'projects/updateproject.html', context)
        return redirect('/')

    else:
        return HttpResponse("Sorry, you do not have permission to edit this project")

