from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>my name is, my name is, my name is</h1>")
def v1(response):
    return HttpResponse("<h1>hello</h1>")