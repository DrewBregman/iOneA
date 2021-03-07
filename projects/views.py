from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Project


class SearchResultsView(ListView):
    model = Project
    template_name = 'search_results.html'