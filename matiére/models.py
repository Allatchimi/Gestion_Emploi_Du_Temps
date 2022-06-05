from django.db import models

# Create your models here.
class matiere(models.Model):
    libelle= models.CharField(max_length=150,null=False)

    def __str__(self):
        return self.libelle