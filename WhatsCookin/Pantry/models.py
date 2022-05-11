from tkinter import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A modle is a class that represents a database table 

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=100, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.name

class Fridge(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True)
    date_stocked = models.DateTimeField(auto_now_add=True, null = True)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    ingredient = models.ManyToManyField(Ingredient, blank = True)

    def __str__(self):
        return self.name