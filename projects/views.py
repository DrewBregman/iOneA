from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Project
from django.db.models import Q
from .forms import MembersForm, CreateForm, ProjectUpdateForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

class SearchResultsView(ListView):
    model = Project
    template_name = 'search_results.html'
    
    def get_queryset(self):
        query=self.request.GET.get('q')
        object_list=Project.objects.filter(
            Q(name__icontains=query) | Q(projectTag__icontains=query)
        )
        object_list1=Project.objects.filter(
            Q(department__icontains=query)
        )
        final_list = list(set(object_list) | set(object_list1))
        return final_list

class SearchPageView(TemplateView):
    template_name = 'searchbar.html'

def createProject(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'projects/projectpage.html')
        return redirect('project')
    else:
        form = CreateForm()
    return render(request, 'projects/createProject.html', {'form': form})

#update projects
@login_required
def project(request):
    #return render(request, 'projects/projectpage.html')
    context = locals()
    template = 'projects/projectpage.html'
    return render (request, template, context)



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

