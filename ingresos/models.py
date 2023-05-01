from django.db import models
from configuracion.models import TipoIngreso,Periodicidad
# Create your models here.


class Ingreso(models.Model):
    fecha=models.DateField(null=False,blank=False)
    tipo=models.ForeignKey(TipoIngreso,on_delete=models.PROTECT,blank=False,null=False)
    detalle=models.CharField(max_length=255,null=False,blank=False)
    monto=models.DecimalField(max_digits=11,decimal_places=2,blank=False,null=False)

    def __str__(self):
        fecha_str = self.fecha.strftime("%d-%b")
        monto_str = "${:,.2f}".format(self.monto).replace(",", ".")
        return f"➕ {fecha_str} | Ingreso por {self.detalle} Total {monto_str}"
    
class IngresoFijo(models.Model):
    detalle=models.CharField(max_length=255,null=False,blank=False)
    tipo=models.ForeignKey(TipoIngreso,on_delete=models.PROTECT,blank=False,null=False)
    periodicidad=models.ForeignKey(Periodicidad,on_delete=models.PROTECT,default=1,blank=False,null=False)
    monto=models.DecimalField(max_digits=11,decimal_places=2,blank=False,null=False)

    def __str__(self):
        return f"{self.detalle} - Periodicidad: {self.periodicidad} - Monto : $ {self.monto}"
    

