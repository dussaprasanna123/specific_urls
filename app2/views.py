from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def secondary(request):
    return HttpResponse('<h1> my brother is my strength</h1>')