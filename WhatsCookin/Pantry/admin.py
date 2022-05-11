from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Ingredient)
admin.site.register(Fridge)
admin.site.register(Customer)
