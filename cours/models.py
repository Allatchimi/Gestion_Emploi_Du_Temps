from django.db import models
from enseignant.models import enseignant
from filiére.models import filiere
from salle.models import salle
from matiére.models import matiere
from groupe.models import groupe
from type.models import type

# Create your models here.
class cours(models.Model):
    Enseignant = models.ForeignKey(enseignant, null=True, on_delete=models.SET_NULL)
    Filiere= models.ForeignKey(filiere, null=True, on_delete=models.SET_NULL)
    Salle = models.ForeignKey(salle, null=True, on_delete=models.SET_NULL)
    Matiere = models.ForeignKey(matiere, null=True, on_delete=models.SET_NULL)
    Groupe = models.ForeignKey(groupe, null=True, on_delete=models.SET_NULL)
    Type = models.ForeignKey(type, null=True, on_delete=models.SET_NULL)
    debut = models.TimeField(null=True)
    fin = models.TimeField(null=True)


