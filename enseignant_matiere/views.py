from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import enseignant_matiere
from .forms import enseignantMRegistration
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listenseignant_matiere(request):
    enseignant_matieres = enseignant_matiere.objects.all()
    context = {'enseignant_matieres': enseignant_matieres}
    return render(request, 'enseignant_matiere/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_enseignant_matiere(request):
    form=enseignantMRegistration()
    if request.method == 'POST':
        form= enseignantMRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enseignant_matiere')
    context ={'form':form}
    return render(request, 'enseignant_matiere/ajouter_enseignant_matiere.html', context)

@login_required(login_url='acces')
def modifier_enseignant_matiere(request,pk):
    enseignant_matieres=enseignant_matiere.objects.get(id=pk)
    form=enseignantMRegistration(instance=enseignant_matieres)
    if request.method == 'POST':
        form= enseignantMRegistration(request.POST, instance=enseignant_matieres)
        if form.is_valid():
            form.save()
            return redirect('enseignant_matiere')
    context ={'form':form }
    return render(request, 'enseignant_matiere/ajouter_enseignant_matiere.html', context)

@login_required(login_url='acces')
def supprimer_enseignant_matiere(request,pk):
    enseignant_matieres = enseignant_matiere.objects.get(id=pk)
    if request.method=='POST':
        enseignant_matieres.delete()
        return redirect('enseignant_matiere')

    context = {'item':enseignant_matieres}
    return render(request, 'enseignant_matiere/supprimer_enseignant_matiere.html', context)