from django.shortcuts import render ,redirect
from cours.models import cours
from enseignant.models import enseignant
from groupe.models import groupe
from matiére.models import matiere
from salle.models import salle
from type.models import type
from classe.models import classe
from filiére.models import filiere
from cours.filters import coursFilters
from django.http import HttpResponse

# Create your views here.
def home(request):

    filieres = filiere.objects.all()
    courss = cours.objects.all()
    classes = classe.objects.all()
    salles = salle.objects.all()
    types = type.objects.all()
    matieres = matiere.objects.all()
    groupes = groupe.objects.all()
    enseignants = enseignant.objects.all()

    total_cours= courss.count()
    total_classe = classes.count()
    total_salle = salles.count()
    total_type = types.count()
    total_matiere = matieres.count()
    total_groupe = groupes.count()
    total_enseignant = enseignants.count()
    total_filiere = filieres.count()
    myFilter =coursFilters(request.GET,queryset= courss)
    courss=myFilter.qs
    context = {'total_filiere':total_filiere,'total_cours':total_cours,
               'total_classe':total_classe,'total_salle':total_salle,
               'total_type':total_type,'total_matiere':total_matiere,
               'total_groupe':total_groupe,'total_enseignant':total_enseignant,
               'courss': courss,'myFilter':myFilter}
    return render(request, 'dashbord/acceuil.html',context)

