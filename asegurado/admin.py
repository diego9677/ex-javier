from django.contrib import admin
from .models import Persona, Asegurado

# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombres', 'apellidos', 'documento_ideentidad', 'fecha_creacion')


@admin.register(Asegurado)
class AseguradoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'persona', 'fecha_nacimiento', 'documento_identidad', 'certificado_nacimiento')
