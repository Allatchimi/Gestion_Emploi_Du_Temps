from django.db import models

# Create your models here.
class annee(models.Model):
    code = models.CharField(max_length=4, null=False)


    def __str__(self):
        return self.code
