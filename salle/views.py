from django.shortcuts import render ,redirect
from .models import salle
from .forms import salleRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='acces')
def listsalle(request):
    salles= salle.objects.all()
    context= { 'salles':salles }
    return render(request, 'salle/addandshow.html',context)


@login_required(login_url='acces')
def ajouter_salle(request):
    form=salleRegistration()
    if request.method == 'POST':
        form= salleRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salle')
    context ={'form':form}
    return render(request, 'salle/ajouter_salle.html', context)

@login_required(login_url='acces')
def modifier_salle(request,pk):
    salles=salle.objects.get(id=pk)
    form=salleRegistration(instance=salles)
    if request.method == 'POST':
        form= salleRegistration(request.POST, instance=salles)
        if form.is_valid():
            form.save()
            return redirect('salle')
    context ={'form':form }
    return render(request, 'salle/ajouter_salle.html', context)

@login_required(login_url='acces')
def supprimer_salle(request,pk):
    salles = salle.objects.get(id=pk)
    if request.method=='POST':
        salles.delete()
        return redirect('salle')

    context = {'item':salles}
    return render(request, 'salle/supprimer_salle.html', context)