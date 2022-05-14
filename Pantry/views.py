from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from .models import *
from Pantry.models import Ingredient
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def Pantry(request):
    if(Ingredient.objects.count() == 0):
        recipes = Recipe.objects.all()
        ingredient = []
        for i in recipes:
            for j in i.ingredients:
                j = j.replace("'","")
                j = j.lstrip()
                j = j.rstrip()
                print(j)
                if j not in ingredient:
                    ingredient.append(str(j))
                    print(len(ingredient))
        counter = 0
        for i in ingredient:
            Ingredient.objects.create(id = counter, name = i).save()
            counter = counter + 1
    ingredients = Ingredient.objects.all()
    context = {
        'Ingredients' : ingredients,
    }
    return render(request, "Pantry/Pantry.html", context)

@login_required(login_url='login')
def AddIngredient(request, id):
    if(request.method == "GET"):
        ingredient = Ingredient.objects.get(id=id)
        if(request.user not in ingredient.is_checked.all()):
            ingredient.is_checked.add(request.user)
        else:
            ingredient.is_checked.remove(request.user)
        ingredients = Ingredient.objects.all()
        context = {
            'Ingredients' : ingredients
        }
        return render(request, "Pantry/Pantry.html", context)
