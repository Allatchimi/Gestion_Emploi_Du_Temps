from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import classe
from .forms import classeRegistration
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listclasse(request):

    classes = classe.objects.all()

    context = {'classes': classes}
    return render(request, 'classe/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_classe(request):
    form=classeRegistration()
    if request.method == 'POST':
        form= classeRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classe')
    context ={'form':form}
    return render(request, 'classe/ajouter_classe.html', context)

@login_required(login_url='acces')
def modifier_classe(request,pk):
    classes=classe.objects.get(id=pk)
    form=classeRegistration(instance=classes)
    if request.method == 'POST':
        form= classeRegistration(request.POST, instance=classes)
        if form.is_valid():
            form.save()
            return redirect('classe')
    context ={'form':form }
    return render(request, 'classe/ajouter_classe.html', context)

@login_required(login_url='acces')
def supprimer_classe(request,pk):
    classes = classe.objects.get(id=pk)
    if request.method=='POST':
        classes.delete()
        return redirect('classe')
    context = {'item':classes}
    return render(request, 'classe/supprimer_classe.html', context)