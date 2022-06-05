from django.db import models
from filiére.models import filiere

# Create your models here.

class classe(models.Model):
    code= models.CharField(max_length=2,null=True)
    id_Filiere= models.ForeignKey(filiere, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.code