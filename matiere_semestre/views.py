from django.shortcuts import render, HttpResponse, redirect
from .models import matiere_semestre
from .forms import matiere_semRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listmatiere_semestre(request):

    matiere_semestres = matiere_semestre.objects.all()

    context = {'matiere_semestres': matiere_semestres}
    return render(request, 'matiere_semestre/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_matiere_semestre(request):
    form=matiere_semRegistration()
    if request.method == 'POST':
        form= matiere_semRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matiere_semestre')
    context ={'form':form}
    return render(request, 'matiere_semestre/ajouter_matiere_semestre.html', context)

@login_required(login_url='acces')
def modifier_matiere_semestre(request,pk):
    matiere_semestres=matiere_semestre.objects.get(id=pk)
    form=matiere_semRegistration(instance=matiere_semestres)
    if request.method == 'POST':
        form= matiere_semRegistration(request.POST, instance=matiere_semestres)
        if form.is_valid():
            form.save()
            return redirect('matiere_semestre')
    context ={'form':form }
    return render(request, 'matiere_semestre/ajouter_matiere_semestre.html', context)

@login_required(login_url='acces')
def supprimer_matiere_semestre(request,pk):
    matiere_semestres = matiere_semestre.objects.get(id=pk)
    if request.method=='POST':
        matiere_semestres.delete()
        return redirect('matiere_semestre')

    context = {'item':matiere_semestres}
    return render(request, 'matiere_semestre/supprimer_matiere_semestre.html', context)