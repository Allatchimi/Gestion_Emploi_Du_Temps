from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import cours

class coursRegistration(ModelForm):
    class Meta:
        model= cours
        fields=  '__all__'
