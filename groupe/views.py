from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required

from .models import groupe
from .forms import groupeRegistration
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listgroupe(request):

    groupes = groupe.objects.all()

    context = {'groupes': groupes}
    return render(request, 'groupe/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_groupe(request):
    form=groupeRegistration()
    if request.method == 'POST':
        form= groupeRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groupe')
    context ={'form':form}
    return render(request, 'groupe/ajouter_groupe.html', context)

@login_required(login_url='acces')
def modifier_groupe(request,pk):
    groupes=groupe.objects.get(id=pk)
    form=groupeRegistration(instance=groupes)
    if request.method == 'POST':
        form= groupeRegistration(request.POST, instance=groupes)
        if form.is_valid():
            form.save()
            return redirect('groupe')
    context ={'form':form }
    return render(request, 'groupe/ajouter_groupe.html', context)

@login_required(login_url='acces')
def supprimer_groupe(request,pk):
    groupes = groupe.objects.get(id=pk)
    if request.method=='POST':
        groupes.delete()
        return redirect('groupe')

    context = {'item':groupes}
    return render(request, 'groupe/supprimer_groupe.html', context)
