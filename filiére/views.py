from django.shortcuts import render, HttpResponse, redirect
from .models import filiere
from .forms import fliereRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listfiliére(request):

    filieres = filiere.objects.all()

    context = {'filieres': filieres}
    return render(request, 'filiére/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_filiere(request):
    form=fliereRegistration()
    if request.method == 'POST':
        form= fliereRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filiére')
    context ={'form':form}
    return render(request, 'filiére/ajouter_filiere.html', context)

@login_required(login_url='acces')
def modifier_filiere(request,pk):
    filieres=filiere.objects.get(id=pk)
    form=fliereRegistration(instance=filieres)
    if request.method == 'POST':
        form= fliereRegistration(request.POST, instance=filieres)
        if form.is_valid():
            form.save()
            return redirect('filiére')
    context ={'form':form }
    return render(request, 'filiére/ajouter_filiere.html', context)

@login_required(login_url='acces')
def supprimer_filiere(request,pk):
    filieres = filiere.objects.get(id=pk)
    if request.method=='POST':
        filieres.delete()
        return redirect('filiére')

    context = {'item':filieres}
    return render(request, 'filiére/supprimer_filiere.html', context)