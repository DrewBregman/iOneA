from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Notification
from django.db.models import Q
from .forms import newUProj
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from main.models import uProjects

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
                             url = 'http://127.0.0.1:8000/agree/' + str(data) + '/' + str(data1))
            n.save()
            return redirect('profile')
    else:
        form = newUProj(request.POST, user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'invite.html', context)
# Create your views here.
def approve(request, username, ProjId):
    return redirect('/Profile')