from django.urls import path
from app2.views import *
app_name='someting'
urlpatterns=[
    path('secondary/',secondary,name='secondary'),
]