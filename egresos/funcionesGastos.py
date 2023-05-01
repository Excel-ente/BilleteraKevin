from .models import  Gasto
from django.contrib import admin
from django.contrib import messages
from django.utils.timezone import datetime, make_aware
from dateutil.relativedelta import relativedelta

@admin.action(description="Pagar gasto Fijo")
def pagar_gasto_fijo(modeladmin, request, queryset):
    # Verificar que solo se haya seleccionado un ingreso fijo
    if queryset.count() != 1:
        message = "Solo puedes pagar de a 1 pago por vez."
        modeladmin.message_user(request, message, level=messages.WARNING)
        return
    
    gasto_fijo = queryset.first()
    
    # Verificar si ya existe un gasto para el mes corriente
    today = datetime.today()
    first_day_month = make_aware(datetime(today.year, today.month, 1))
    last_day_month = make_aware(datetime(today.year, today.month, 1) + relativedelta(months=1, days=-1))
    gasto_mes_corriente = Gasto.objects.filter(
        tipo=gasto_fijo.tipo,
        fecha__range=[first_day_month, last_day_month]
    )
    if gasto_mes_corriente.exists():
        message = f"Ya existe un ingreso para {gasto_fijo.detalle} en el mes corriente."
        modeladmin.message_user(request, message, level=messages.ERROR)
        return
    
    # Crear un nuevo registro de ingreso
    nuevo_gasto = Gasto.objects.create(
        fecha=datetime.now(),
        tipo=gasto_fijo.tipo,
        detalle=gasto_fijo.detalle,
        monto=gasto_fijo.valor_cuota
    )
    
    message = f"Se ha generado un nuevo ingreso por ${nuevo_gasto.monto} para {nuevo_gasto.detalle}."
    modeladmin.message_user(request, message, level=messages.SUCCESS)