from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from .models import type
from .forms import typeRegistration
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listtype(request):

    types = type.objects.all()

    context = {'types': types}
    return render(request, 'type/addandshow.html', context)

@login_required(login_url='acces')
def ajouter_type(request):
    form=typeRegistration()
    if request.method == 'POST':
        form= typeRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type')
    context ={'form':form}
    return render(request, 'type/ajouter_type.html', context)

@login_required(login_url='acces')
def modifier_type(request,pk):
    types=type.objects.get(id=pk)
    form=typeRegistration(instance=types)
    if request.method == 'POST':
        form= typeRegistration(request.POST, instance=types)
        if form.is_valid():
            form.save()
            return redirect('type')
    context ={'form':form }
    return render(request, 'type/ajouter_type.html', context)

@login_required(login_url='acces')
def supprimer_type(request,pk):
    types = type.objects.get(id=pk)
    if request.method=='POST':
        types.delete()
        return redirect('type')

    context = {'item':types}
    return render(request, 'type/supprimer_type.html', context)