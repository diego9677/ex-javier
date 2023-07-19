from django import forms
from .models import Contrato

form_control = 'rounded-md outline-none px-2 py-1 ring-1 ring-neutral-300 focus:ring-blue-600 focus:ring-2'


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ('titulo', 'descripcion', 'precio_seguro',
                  'precio_dependiente', 'fecha_inicio', 'fecha_fin', 'estado',)
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'precio_seguro': 'P. Seguro',
            'precio_dependiente': 'P. Dependiente',
            'fecha_inicio': 'Fecha Inicio',
            'fecha_fin': 'Fecha Fin',
            'estado': 'Estado'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': form_control}),
            'descripcion': forms.Textarea(attrs={'class': form_control, 'cols': 10, 'rows': 3}),
            'precio_seguro': forms.NumberInput(attrs={'class': form_control}),
            'precio_dependiente': forms.NumberInput(attrs={'class': form_control}),
            'fecha_inicio': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': form_control, 'type': 'date'},

            ),
            'fecha_fin': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': form_control, 'type': 'date'}
            ),
            'estado': forms.NumberInput(attrs={'class': form_control}),
        }
