from django.shortcuts import render,redirect

from .models import annee
from .forms import anneeRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listannee(request):

    annees = annee.objects.all()

    context = {'annees': annees}
    return render(request, 'annee/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_annee(request):
    form=anneeRegistration()
    if request.method == 'POST':
        form= anneeRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ann')
    context ={'form':form}
    return render(request, 'annee/ajouter_annee.html', context)

@login_required(login_url='acces')
def modifier_annee(request,pk):
    annees=annee.objects.get(id=pk)
    form=anneeRegistration(instance=annees)
    if request.method == 'POST':
        form= anneeRegistration(request.POST, instance=annees)
        if form.is_valid():
            form.save()
            return redirect('ann')
    context ={'form':form }
    return render(request, 'annee/ajouter_annee.html', context)

@login_required(login_url='acces')
def supprimer_annee(request,pk):
    annees = annee.objects.get(id=pk)
    if request.method=='POST':
        annees.delete()
        return redirect('ann')

    context = {'item':annees}
    return render(request, 'annee/supprimer_annee.html', context)