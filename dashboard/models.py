from django.db import models
from ingresos.models import Ingreso
from egresos.models import Gasto
from django.db.models import Sum
# Create your models here.

class CajaCentral(models.Model):
    nombre=models.CharField(max_length=50,default="Ver detealle",blank=True,null=True)
    ingresos=models.DecimalField(max_digits=11,decimal_places=0,blank=True,null=True)
    gastos=models.DecimalField(max_digits=11,decimal_places=0,blank=True,null=True)
    saldo_en_caja=models.DecimalField(max_digits=11,decimal_places=0,blank=True,null=True)
    
    def __str__(self):
        return f"Caja central $ {self.saldo_en_caja} | VER DETALLE 🔍"
    
    class Meta:
        verbose_name = 'Mi Billetera'
        verbose_name_plural ='Mi Billetera'

    def save(self, *args, **kwargs):

        self.ingresos = Ingreso.objects.aggregate(total_ingreso=Sum('monto'))['total_ingreso'] or 0

        self.gastos = Gasto.objects.aggregate(total_gasto=Sum('monto'))['total_gasto'] or 0

        self.saldo_en_caja = self.ingresos - self.gastos

        super(CajaCentral, self).save(*args, **kwargs)