from django.contrib import admin
from .models import CajaCentral
from .funcion import ActualizarCaja
# Register your models here.


@admin.register(CajaCentral)
class CajaCentralAdmin(admin.ModelAdmin):
    list_display=('_','Ingresos','Egresos','Total_Caja',)
    readonly_fields=('Ingresos','Egresos','Total_Caja',)
    exclude=('nombre','ingresos','gastos','saldo_en_caja',)
    actions=(ActualizarCaja,)

    def _(self,obj):
        return obj.nombre
    
    def Ingresos(self, obj):
        return "💵 ${:,.2f}".format(obj.ingresos)
    
    def Egresos(self, obj):
        return "💵 ${:,.2f}".format(obj.gastos)
    
    def Total_Caja(self, obj):
        return "💵 ${:,.2f}".format(obj.saldo_en_caja)