from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import semestre

class semestreRegistration(ModelForm):
    class Meta:
        model= semestre
        fields=  '__all__'
