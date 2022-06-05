from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import annee

class anneeRegistration(ModelForm):
    class Meta:
        model= annee
        fields=  '__all__'
