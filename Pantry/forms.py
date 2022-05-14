from django import forms
from django.contrib.auth.models import User
from Pantry.models import Ingredients

class IngredientsForm(forms.ModelForm):
    is_checked = forms.BooleanField()

    class Meta:
        model = Ingredients
