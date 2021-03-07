from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('search/',views.search,name='search'),
    path('myprofile',views.myprofile,name='myprofile'),
]