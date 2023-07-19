from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento_ideentidad = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def  __str__(self) -> str:
        return f'{self.nombres} {self.apellidos}'



class Asegurado(models.Model):
    persona = models.OneToOneField(Persona, related_name='asegurado', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='uploads/fotos')
    fecha_nacimiento = models.DateField()
    certificado_nacimiento = models.ImageField(upload_to='uploads/certificados')
    documento_identidad = models.ImageField(upload_to='uploads/identificacion')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='asegurado', on_delete=models.SET_NULL)

    def  __str__(self) -> str:
        return f'{self.persona.nombres} {self.persona.apellidos}'
