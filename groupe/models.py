from django.db import models
from classe.models import classe
# Create your models here.
class groupe(models.Model):
    code = models.CharField(max_length=11, null=False)
    capacite = models.IntegerField(null=False)
    id_classe = models.ForeignKey(classe, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.code


