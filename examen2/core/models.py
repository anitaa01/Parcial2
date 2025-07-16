from django.db import models
from django.contrib.auth.models import User

class Pendiente(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    resuelto = models.BooleanField(default=False, verbose_name="Resuelto")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Pendiente"
        verbose_name_plural = "Pendientes"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.id} - {self.title} ({'Resuelto' if self.resuelto else 'Pendiente'})"