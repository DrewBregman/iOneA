from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Notification
from django.db.models import Q


class SearchResultsView(ListView):
    model = Notification
    template_name = 'noti.html'

    def get_queryset(self):
        return Notification.objects.filter(user = self.request.user)

# Create your views here.
