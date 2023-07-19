from django import forms
from .models import Asegurado
from contrato.models import Contrato

form_control = 'rounded-md outline-none px-2 py-1 ring-1 ring-neutral-300 focus:ring-blue-600 focus:ring-2'


class AseguradoForm(forms.Form):
    nombres = forms.CharField(
        max_length=200,
        label='Nombres',
        widget=forms.TextInput(
            attrs={
                'class': form_control},
        )
    )
    apellidos = forms.CharField(
        max_length=200,
        label='Apellidos',
        widget=forms.TextInput(
            attrs={
                'class': form_control},
        )
    )
    ci = forms.CharField(
        max_length=50,
        label='CI',
        widget=forms.TextInput(
            attrs={
                'class': form_control},
        )
    )

    fecha_nacimiento = forms.DateField(
        label='Fecha Nacimiento',
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'type': 'date',
                'class': form_control
            },
        )
    )
    foto = forms.ImageField(
        label='Foto',
    )
    certificado_nacimiento = forms.ImageField(label='Certificado Nacimiento')
    documento_identidad = forms.ImageField(label='Documento de identidad')
    parent = forms.ModelChoiceField(
        label='Depende de',
        queryset=Asegurado.objects.all(),
        widget=forms.Select(
            attrs={
                'class': form_control}
        ),
        required=False
    )
    contratos = forms.ModelMultipleChoiceField(
        queryset=Contrato.objects.all(),
        label='Contratos',
        widget=forms.SelectMultiple(
            attrs={'class': form_control}
        )
    )