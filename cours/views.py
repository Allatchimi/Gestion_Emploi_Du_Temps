from django.shortcuts import render, HttpResponse, redirect
from .models import cours
from .forms import coursRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listcours(request):

    courss = cours.objects.all()

    context = {'courss': courss}
    return render(request, 'cours/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_cours(request):
    form=coursRegistration()
    if request.method == 'POST':
        form= coursRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours')
    context ={'form':form}
    return render(request, 'cours/ajouter_cours.html', context)

@login_required(login_url='acces')
def modifier_cours(request,pk):
    courss=cours.objects.get(id=pk)
    form=coursRegistration(instance=courss)
    if request.method == 'POST':
        form= coursRegistration(request.POST, instance=courss)
        if form.is_valid():
            form.save()
            return redirect('cours')
    context ={'form':form }
    return render(request, 'cours/ajouter_cours.html', context)

@login_required(login_url='acces')
def supprimer_cours(request,pk):
    courss = cours.objects.get(id=pk)
    if request.method=='POST':
        courss.delete()
        return redirect('cours')

    context = {'item':courss}
    return render(request, 'cours/supprimer_cours.html', context)