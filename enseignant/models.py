from django.db import models

# Create your models here.
class enseignant(models.Model):
    nom= models.CharField(max_length=150,null=True)
    prenom= models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.nom