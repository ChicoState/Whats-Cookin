"""WhatsCookin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import include, path
from Home import views as home_views
from Popular import views as popular_views
from Edamam import views as edamam_views
from pantry import views as pantry_views
from Random import views as random_views

def customer(request):
    return HttpResponse('Customer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_views.Home,name='Home'),
    path('Popular/',popular_views.Popular),
    path('Pantry/', pantry_views.Pantry),
    path('Recipe/', edamam_views.User_Recipe),
    path('Random/', random_views.Random),
    path('', include('accounts.urls')),
    path('', include('pantry.urls')),
]
