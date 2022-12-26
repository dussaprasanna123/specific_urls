from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>my daddy is my hero<h1>')
def prasanna(request):
    return HttpResponse('<h1>prasanna is a good girl</h1>')