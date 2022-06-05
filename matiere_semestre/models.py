from django.db import models
from matiére.models import matiere
from semestre.models import semestre
from filiére.models import filiere
from type.models import type
# Create your models here.
class matiere_semestre(models.Model):
    id_Matiere = models.ForeignKey(matiere, null=True, on_delete=models.SET_NULL)
    id_Semestre = models.ForeignKey(semestre, null=True, on_delete=models.SET_NULL)
    id_Filiere = models.ForeignKey(filiere, null=True, on_delete=models.SET_NULL)
    id_Type = models.ForeignKey(type, null=True, on_delete=models.SET_NULL)
    heure= models.IntegerField(null=False)




