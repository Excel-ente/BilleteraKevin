from .models import  Ingreso
from django.contrib import admin
from django.contrib import messages
from django.utils.timezone import datetime, make_aware
from dateutil.relativedelta import relativedelta

@admin.action(description="Cobrar Ingreso Fijo")
def cobrar_ingreso_fijo(modeladmin, request, queryset):
    # Verificar que solo se haya seleccionado un ingreso fijo
    if queryset.count() != 1:
        message = "Debe seleccionar exactamente 1 ingreso fijo."
        modeladmin.message_user(request, message, level=messages.WARNING)
        return
    
    ingreso_fijo = queryset.first()
    
    # Verificar si ya existe un ingreso para el mes corriente
    today = datetime.today()
    first_day_month = make_aware(datetime(today.year, today.month, 1))
    last_day_month = make_aware(datetime(today.year, today.month, 1) + relativedelta(months=1, days=-1))
    ingresos_mes_corriente = Ingreso.objects.filter(
        tipo=ingreso_fijo.tipo,
        fecha__range=[first_day_month, last_day_month]
    )
    if ingresos_mes_corriente.exists():
        message = f"Ya existe un ingreso para {ingreso_fijo.detalle} en el mes corriente."
        modeladmin.message_user(request, message, level=messages.ERROR)
        return
    
    # Crear un nuevo registro de ingreso
    nuevo_ingreso = Ingreso.objects.create(
        fecha=datetime.now(),
        tipo=ingreso_fijo.tipo,
        detalle=ingreso_fijo.detalle,
        monto=ingreso_fijo.monto
    )
    
    message = f"Se ha generado un nuevo ingreso por ${nuevo_ingreso.monto} para {nuevo_ingreso.detalle}."
    modeladmin.message_user(request, message, level=messages.SUCCESS)