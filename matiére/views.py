from django.shortcuts import render ,redirect
from matiére.models import matiere
from .forms import matiereRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listmatiére(request):
    matieres= matiere.objects.all()
    context= { 'matieres':matieres }
    return render(request, 'matiére/addandshow.html',context)


@login_required(login_url='acces')
def ajouter_matiere(request):
    form=matiereRegistration()
    if request.method == 'POST':
        form= matiereRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matiére')
    context ={'form':form}
    return render(request, 'matiére/ajouter_matiere.html', context)

@login_required(login_url='acces')
def modifier_matiere(request,pk):
    matieres=matiere.objects.get(id=pk)
    form=matiereRegistration(instance=matieres)
    if request.method == 'POST':
        form= matiereRegistration(request.POST, instance=matieres)
        if form.is_valid():
            form.save()
            return redirect('matiére')
    context ={'form':form }
    return render(request, 'matiére/ajouter_matiere.html', context)

@login_required(login_url='acces')
def supprimer_matiere(request,pk):
    matieres = matiere.objects.get(id=pk)
    if request.method=='POST':
        matieres.delete()
        return redirect('matiére')

    context = {'item':matieres}
    return render(request, 'matiére/supprimer_matiere.html', context)