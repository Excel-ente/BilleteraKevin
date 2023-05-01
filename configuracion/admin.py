from django.contrib import admin
from .models import TipoGasto,TipoIngreso,Periodicidad
# Register your models here.

admin.site.register(TipoGasto)

admin.site.register(TipoIngreso)

admin.site.register(Periodicidad)