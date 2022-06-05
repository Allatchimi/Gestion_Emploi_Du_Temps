from django.db import models
# Create your models here.

class filiere(models.Model):
    libelle= models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.libelle

