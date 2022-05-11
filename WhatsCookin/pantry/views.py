from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

from .models import *
from .forms import FridgeForm

# Create your views here.
# Views define how the html page will render and look. they use data from the model
@login_required(login_url='login')
def Pantry(request):
    return render(request, "Pantry/Pantry.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createFridge(request):

    form = FridgeForm()
    if request.method == 'POST':
        form = FridgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'pantry/updateFridge.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def updateFridge(request, pri_key):

    fridge = Fridge.objects.get(id=pri_key)
    form = FridgeForm(instance=fridge)

    if request.method == 'POST':
        form = FridgeForm(request.POST, instance=fridge)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'pantry/updateFridge.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def deleteFridge(request, pri_key):
	fridge = Fridge.objects.get(id=pri_key)
	if request.method == "POST":
		fridge.delete()
		return redirect('dashboard')

	context = {'item':fridge}
	return render(request, 'pantry/deleteFridge.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def dashboard(request):
    fridges = request.user.customer.fridge_set.all() # related set 
    fridge_count = fridges.count()
    customer = request.user.customer
    if fridge_count > 0:
        ingredient_count = request.user.customer.fridge_set.first().ingredient.count() #only working with one fridge
    else:
        ingredient_count = 0
    
    context = {'fridges':fridges, 'fridge_count':fridge_count, 'customer':customer, 
    'ingredient_count':ingredient_count}
    return render(request, 'pantry/dashboard.html', context)
