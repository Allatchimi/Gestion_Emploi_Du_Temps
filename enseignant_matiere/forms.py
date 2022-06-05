from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import enseignant_matiere

class enseignantMRegistration(ModelForm):
    class Meta:
        model= enseignant_matiere
        fields=  '__all__'
