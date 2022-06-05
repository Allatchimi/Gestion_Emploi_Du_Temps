from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import filiere

class fliereRegistration(ModelForm):
    class Meta:
        model= filiere
        fields=  '__all__'
