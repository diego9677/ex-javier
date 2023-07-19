from django.db import models

# Create your models here.


class Contrato(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_seguro = models.DecimalField(max_digits=18, decimal_places=2)
    precio_dependiente = models.DecimalField(max_digits=18, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.IntegerField()

    def __str__(self) -> str:
        return self.titulo


class PlanPago(models.Model):
    fecha_vencimiento = models.DateField()
    monto = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )
    contrato = models.ForeignKey(
        Contrato,
        related_name='plan_pago',
        on_delete=models.SET_NULL,
        null=True
    )
