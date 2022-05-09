from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def Pantry(request):
    return render(request,"Pantry/Pantry.html")
