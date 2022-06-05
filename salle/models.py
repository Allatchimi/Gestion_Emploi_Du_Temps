from django.db import models

# Create your models here.
class salle(models.Model):
    code= models.CharField(max_length=150,null=True)
    capacite=models.IntegerField(null=True)
    pc=models.IntegerField(null=True)
    def __str__(self):
        return self.code
