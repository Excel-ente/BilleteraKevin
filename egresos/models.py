from django.db import models
from configuracion.models import TipoGasto,Periodicidad



class Gasto(models.Model):
    fecha=models.DateField(null=False,blank=False)
    tipo=models.ForeignKey(TipoGasto,on_delete=models.PROTECT,blank=False,null=False)
    detalle=models.CharField(max_length=255,null=False,blank=False)
    monto=models.DecimalField(max_digits=11,decimal_places=2,blank=False,null=False)

    def __str__(self):
        fecha_str = self.fecha.strftime("%d-%b")
        monto_str = "${:,.2f}".format(self.monto).replace(",", ".")
        return f"➖ {fecha_str} | Gasto por {self.detalle} Total {monto_str}"
    
class GastoFijo(models.Model):
    estado=models.BooleanField(verbose_name="Activo",default=True)
    detalle=models.CharField(max_length=255,null=False,blank=False)
    tipo=models.ForeignKey(TipoGasto,on_delete=models.PROTECT,blank=False,null=False)
    fecha_primer_pago=models.DateField(blank=False,null=False)
    cuotas=models.IntegerField(default=1,blank=False,null=False)
    valor_cuota=models.DecimalField(max_digits=11,decimal_places=2,blank=False,null=False)
    cuotas_pagas=models.IntegerField(default=0,blank=False,null=False)
    cuotas_restantes=models.IntegerField(default=0,blank=False,null=False)

    def __str__(self):
        return f"{self.detalle} - Cuotas: {self.cuotas} - Monto : $ {self.valor_cuota}"
    

