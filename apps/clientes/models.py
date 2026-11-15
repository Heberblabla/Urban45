"""
Archivo: apps/clientes/models.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Descripción: Modelo Cliente (Programación Orientada a Objetos) que representa
             a los socios inscritos en el gimnasio Urban 45.
"""

from django.db import models


class Cliente(models.Model):
    """Representa a un cliente o socio registrado en Urban 45."""

    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def obtener_nombre_completo(self):
        """Devuelve el nombre y apellido completo del socio."""
        return f"{self.nombre} {self.apellidos}".strip()

    def __str__(self):
        return f"{self.obtener_nombre_completo()} (DNI: {self.dni})"
