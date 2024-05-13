from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
                'name': TextInput(attrs = {'class': 'input', 'placeholder': 'Search City...'}),
                }

