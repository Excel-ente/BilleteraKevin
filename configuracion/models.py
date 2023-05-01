from django.db import models

# Create your models here.
class TipoGasto(models.Model):
    detalle=models.CharField(max_length=50,null=False,blank=False,unique=True)

    def __str__(self):
        return self.detalle

class TipoIngreso(models.Model):
    detalle=models.CharField(max_length=50,null=False,blank=False,unique=True)

    def __str__(self):
        return self.detalle
    
class Periodicidad(models.Model):
    detalle=models.CharField(max_length=50,null=False,blank=False,unique=True)

    def __str__(self):
        return self.detalle