from django.shortcuts import render, HttpResponse, redirect
from .models import enseignant
from .forms import enseignantRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listenseignant(request):

    enseignants = enseignant.objects.all()

    context = {'enseignants': enseignants}
    return render(request, 'enseignant/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_enseignant(request):
    form=enseignantRegistration()
    if request.method == 'POST':
        form= enseignantRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enseignant')
    context ={'form':form}
    return render(request, 'enseignant/ajouter_enseignant.html', context)

@login_required(login_url='acces')
def modifier_enseignant(request,pk):
    enseignants=enseignant.objects.get(id=pk)
    form=enseignantRegistration(instance=enseignants)
    if request.method == 'POST':
        form= enseignantRegistration(request.POST, instance=enseignants)
        if form.is_valid():
            form.save()
            return redirect('enseignant')
    context ={'form':form }
    return render(request, 'enseignant/ajouter_enseignant.html', context)

@login_required(login_url='acces')
def supprimer_enseignant(request,pk):
    enseignants = enseignant.objects.get(id=pk)
    if request.method=='POST':
        enseignants.delete()
        return redirect('enseignant')

    context = {'item':enseignants}
    return render(request, 'enseignant/supprimer_enseignant.html', context)