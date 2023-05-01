from django.contrib import admin
from .models import Gasto,GastoFijo
from .funcionesGastos import pagar_gasto_fijo   
#from .funciones import cobrar_ingreso_fijo


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display=('fecha','tipo','detalle','Total',) 

    def Total(self, obj):
        return "💵 ${:,.2f}".format(obj.monto)

@admin.register(GastoFijo)
class GastoFijoAdmin(admin.ModelAdmin):
    list_display=('detalle','tipo','Valor_Total','cuotas_restantes',) 
    exclude=('cuotas_pagas','cuotas_restantes',)
    actions=[pagar_gasto_fijo,]

    def Valor_Total(self, obj):
        return "💵 ${:,.2f}".format(obj.valor_cuota)