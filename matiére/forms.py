from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import matiere

class matiereRegistration(ModelForm):
    class Meta:
        model= matiere
        fields=  '__all__'
