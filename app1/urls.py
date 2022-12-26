from django.urls import path
from app1.views import *
app_name='someting'
urlpatterns=[
    path('first/',first,name='first'),
    path('prasanna/',prasanna,name='prasanna'),
]