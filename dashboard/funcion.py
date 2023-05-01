from .models import CajaCentral
from django.contrib import admin,messages

@admin.action(description="Actualizar mi billetera")
def ActualizarCaja(modeladmin, request, queryset):

    Caja = CajaCentral.objects.all()

    for x in Caja:
        x.save()

    message = "Tu billetera ha sido actualizada."
    modeladmin.message_user(request, message, level=messages.SUCCESS)