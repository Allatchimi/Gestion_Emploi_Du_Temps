from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import type

class typeRegistration(ModelForm):
    class Meta:
        model= type
        fields=  '__all__'
