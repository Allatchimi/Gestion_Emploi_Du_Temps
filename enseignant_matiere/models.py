from django.db import models
from matiére.models import matiere
from enseignant.models import enseignant

# Create your models here.
class enseignant_matiere(models.Model):
    id_Matiere = models.ForeignKey(matiere, null=True, on_delete=models.SET_NULL)
    id_Enseignant = models.ForeignKey(enseignant, null=True, on_delete=models.SET_NULL)


