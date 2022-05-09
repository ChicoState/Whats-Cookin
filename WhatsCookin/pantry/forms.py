from django.forms import ModelForm
from .models import *

#

class FridgeForm(ModelForm):
    class Meta:
        model = Fridge
        fields = '__all__'