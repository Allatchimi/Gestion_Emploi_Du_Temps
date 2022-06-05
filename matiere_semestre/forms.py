from django.core import validators
from django.forms import ModelForm
from django import forms
from  .models import matiere_semestre

class matiere_semRegistration(ModelForm):
    class Meta:
        model= matiere_semestre
        fields=  '__all__'
