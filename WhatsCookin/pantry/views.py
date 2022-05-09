from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import FridgeForm

# Create your views here.
# Views define how the html page will render and look. they use data from the model


@login_required(login_url='login')
def dashboard(request, pri_key):
    customer = Customer.objects.get(id=pri_key)

    fridges = customer.fridge_set.all() # related set 
    fridge_count = fridges.count()

    ingredient_count = customer.fridge_set.first().ingredient.count() #only working with one fridge

    context = {'customer':customer, 'fridges':fridges, 'fridge_count':fridge_count, 'ingredient_count':ingredient_count}
    return render(request, 'pantry/dashboard.html', context)

@login_required(login_url='login')
def createFridge(request):

    form = FridgeForm()
    if request.method == 'POST':
        form = FridgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pantry/dashboard.html')

    context = {'form':form}
    return render(request, 'pantry/createFridge.html', context)

@login_required(login_url='login')
def updateFridge(request, cust_key, fri_key):

    fridge = Fridge.objects.get(id=fri_key)
    form = FridgeForm(instance=fridge)

    if request.method == 'POST':
        form = FridgeForm(request.POST, instance=fridge)
        if form.is_valid():
            form.save()
            return redirect('dashboard', pri_key=cust_key)

    context = {'form':form}
    return render(request, 'pantry/updateFridge.html', context)

@login_required(login_url='login')
def deleteFridge(request, cust_key, fri_key):
	fridge = Fridge.objects.get(id=pri_key)
	if request.method == "POST":
		fridge.delete()
		return redirect('dashboard', pri_key=cust_key)

	context = {'item':fridge}
	return render(request, 'pantry/deleteFridge.html', context)
