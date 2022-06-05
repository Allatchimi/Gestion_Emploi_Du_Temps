from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import semestre
from .forms import semestreRegistration
# Create your views here.

from django.http import HttpResponse
@login_required(login_url='acces')
def listsemestre(request):

    semestres = semestre.objects.all()

    context = {'semestres': semestres}
    return render(request, 'semestre/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_semestre(request):
    form=semestreRegistration()
    if request.method == 'POST':
        form= semestreRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semestre')
    context ={'form':form}
    return render(request, 'semestre/ajouter_semestre.html', context)

@login_required(login_url='acces')
def modifier_semestre(request,pk):
    semestres= semestre.objects.get(id=pk)
    form=semestreRegistration(instance=semestres)
    if request.method == 'POST':
        form= semestreRegistration(request.POST, instance=semestres)
        if form.is_valid():
            form.save()
            return redirect('semestre')
    context ={'form':form }
    return render(request, 'semestre/ajouter_semestre.html', context)

@login_required(login_url='acces')
def supprimer_semestre(request,pk):
    semestres = semestre.objects.get(id=pk)
    if request.method=='POST':
        semestres.delete()
        return redirect('semestre')

    context = {'item':semestres}
    return render(request, 'semestre/supprimer_semestre.html', context)