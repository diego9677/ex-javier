from django import forms
from .models import Contrato


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ('titulo', 'descripcion', 'precio_seguro',
                  'precio_dependiente', 'fecha_inicio', 'fecha_fin', 'estado',)
