from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Project
from django.db.models import Q

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
