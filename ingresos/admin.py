from django.contrib import admin
from .models import *
from .funciones import cobrar_ingreso_fijo
# Register your models here.

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display=('fecha','tipo','detalle','Total',) 

    def Total(self, obj):
        return "💵 ${:,.2f}".format(obj.monto)

@admin.register(IngresoFijo)
class IngresoFijoAdmin(admin.ModelAdmin):
    list_display=('detalle','tipo','periodicidad','monto',) 
    actions=[cobrar_ingreso_fijo,]