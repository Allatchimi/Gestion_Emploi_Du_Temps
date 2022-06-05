from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import salle

class salleRegistration(ModelForm):
    class Meta:
        model= salle
        fields=  '__all__'
