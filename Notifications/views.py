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
class SearchResultsView(ListView):
    model = Notification
    template_name = 'noti.html'

    def get_queryset(self):
        return Notification.objects.filter(user = self.request.user)

def invite(request):
    if request.method == "POST":
        form = newUProj(request.POST, instance=request.user)
        if form.is_valid():
            data = form.cleaned_data.get("user")
            form.save()
            #messages.success(request, f'Your account has been updated!')
            n = Notification(user = data, message = "You have a new project request")
            n.save()
            return redirect('profile')
    else:
        form = newUProj(request.POST, instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'invite.html', context)
# Create your views here.
