"""
Archivo: apps/entrenamientos/models.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Descripción: Modelos RutinaEntrenamiento y ProgresoCliente para asignar planes
             personalizados y registrar avances de fuerza/repeticiones.
"""

from django.db import models


class RutinaEntrenamiento(models.Model):
    """Representa una rutina de ejercicios asignada a un socio."""

    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
        related_name="rutinas",
    )
    nombre_rutina = models.CharField(max_length=100)
    objetivo_cliente = models.CharField(max_length=80)
    condicion_fisica = models.CharField(max_length=50)
    entrenador_asignado = models.CharField(max_length=80, default="Entrenador Urban 45")
    fecha_asignacion = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "rutina_entrenamiento"
        verbose_name = "Rutina de Entrenamiento"
        verbose_name_plural = "Rutinas de Entrenamiento"

    def __str__(self):
        return f"{self.nombre_rutina} -> {self.cliente.obtener_nombre_completo()}"


class ProgresoCliente(models.Model):
    """Registra una sesión de avance físico (peso levantado y repeticiones)."""

    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
        related_name="progresos",
    )
    fecha = models.DateField()
    peso_levantado_kg = models.DecimalField(max_digits=6, decimal_places=2)
    repeticiones = models.PositiveIntegerField()
    comentario = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "progreso_cliente"
        verbose_name = "Progreso de Cliente"
        verbose_name_plural = "Progresos de Clientes"

    def __str__(self):
        return f"{self.cliente.obtener_nombre_completo()} ({self.fecha}: {self.peso_levantado_kg} kg)"
