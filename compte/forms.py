from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreerUtilisateur(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Entrer votre nom'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Entrer votre mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Entrer votre mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirmer votre mot de passe'}))
    class Meta:
        model = User
        fields= ['username','email','password1','password2']
