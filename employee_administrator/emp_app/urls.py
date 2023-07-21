"""
URL configuration for employee_administrator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    # no need to add () after index .. name is sufficient
    path('', views.index, name = 'index'),
    # now here we need to create function in views.py so that it routes 
    
    path('all_emp', views.index, name = 'all_emp'),
    path('add_emp', views.index, name = 'add_emp'),
    path('remove_emp', views.index, name = 'remove_emp'),
    path('filter_emp', views.index, name = 'filter_emp'),
    # for simplicity i have given the function name same as the names
]
