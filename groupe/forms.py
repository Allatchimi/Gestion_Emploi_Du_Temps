from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import groupe

class groupeRegistration(ModelForm):
    class Meta:
        model= groupe
        fields=  '__all__'
