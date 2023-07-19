from django import forms
from .models import Asegurado, Persona


class AseguradoForm(forms.Form):
    nombres = forms.CharField(
        max_length=200,
        label='Nombres',
        widget=forms.TextInput(
            attrs={
                'class': 'rounded-md outline-none px-2 py-1 ring-1 ring-neutral-300 focus:ring-blue-600 focus:ring-2'},
        )
    )
    apellidos = forms.CharField(
        max_length=200,
        label='Apellidos',
        widget=forms.TextInput(
            attrs={
                'class': 'rounded-md outline-none px-2 py-1 ring-1 ring-neutral-300 focus:ring-blue-600 focus:ring-2'},
        )
    )
    ci = forms.CharField(
        max_length=50,
        label='CI',
        widget=forms.TextInput(
            attrs={
                'class': 'rounded-md outline-none px-2 py-1 ring-1 ring-neutral-300 focus:ring-blue-600 focus:ring-2'},
        )
    )

    fecha_nacimiento = forms.DateField(
        label='Fecha Nacimiento',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'rounded-md outline-none px-2 py-1 ring-1 ring-neutral-300 focus:ring-blue-600 focus:ring-2'
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
                'class': 'rounded-md outline-none px-2 py-1 ring-1 ring-neutral-300 focus:ring-blue-600 focus:ring-2'}
        ),
        required=False
    )
