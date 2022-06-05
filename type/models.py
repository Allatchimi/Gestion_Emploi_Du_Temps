from django.db import models

# Create your models here.
class type(models.Model):
    libelle = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.libelle
