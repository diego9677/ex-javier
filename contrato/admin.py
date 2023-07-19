from django.contrib import admin
from .models import Contrato, PlanPago

# Register your models here.

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'titulo', 'precio_seguro', 'precio_dependiente', 'fecha_inicio', 'fecha_fin', 'estado')


@admin.register(PlanPago)
class PlanPagoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fecha_vencimiento', 'monto')
