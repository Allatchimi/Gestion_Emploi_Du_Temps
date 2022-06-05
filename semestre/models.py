from django.db import models
from annee.models import annee
# Create your models here.
class semestre(models.Model):
    code = models.CharField(max_length=3, null=True)
    id_Annee = models.ForeignKey(annee,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.code