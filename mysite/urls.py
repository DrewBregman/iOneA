"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as v
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Notifications import views as n
from django.conf.urls import url
from projects import views as p
from posts import views as q

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',v.register, name='register'),
    path('profile/<int:id>/',v.profile, name='profile1'),
    path('profile/',v.profile1, name='profile'),
    path('home/',v.home, name='home'),
    path('notifications/',n.Notifications, name='noti'),
    path('invite/',n.invite, name='invite'),
    path('accept/<str:name1>/<int:id>/', n.accept, name='accept'),
    path('project/<str:name>/request/<int:id>', n.request, name= 'request'),
    path('allow/<str:name1>/<int:id>/', n.allow, name = 'allow'),
    path('', include('main.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', include('projects.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    #url(r'^updateprofile', v.updateprofile),
    path('updateprofile/', v.updateprofile, name='updateprofile'),
    path('createproject/', p.createProject, name='createproject'),
    path('project/<str:name>/', p.project, name='project'),
    path('editproject/<str:name>/', p.update, name="editproject"),
    #path('editproject/', v.home, name="editproject"),
    path('agree/', include('Notifications.urls')),
    path('posts/', q.placeholder, name="postplaceholder"),
    path('myprojects/', p.myProjects, name="myprojects"),
   
]   
# /home/start
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
