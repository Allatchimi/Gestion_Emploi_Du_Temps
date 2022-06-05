from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import enseignant

class enseignantRegistration(ModelForm):
    class Meta:
        model= enseignant
        fields=  '__all__'
