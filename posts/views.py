from django.shortcuts import render
from django.http import HttpResponse

def placeholder(request):
    return HttpResponse("This is a placeholder")