from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
path('email/',views.emailView,name='email'),
path('success/',views.successView,name='success'),
path('thanks/',views.thanksView,name='thanks'),
path('project_list/',views.projectView,name='projectView'),
]