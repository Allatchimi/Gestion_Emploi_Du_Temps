from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import classe

class classeRegistration(ModelForm):
    class Meta:
        model= classe
        fields=  '__all__'
