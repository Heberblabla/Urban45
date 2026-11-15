"""
Archivo: apps/entrenamientos/admin.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Registro de modelos de rutinas y progreso en el admin de Django.
"""

from django.contrib import admin
from .models import ProgresoCliente, RutinaEntrenamiento


@admin.register(RutinaEntrenamiento)
class RutinaEntrenamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre_rutina", "cliente", "objetivo_cliente", "condicion_fisica", "fecha_asignacion")


@admin.register(ProgresoCliente)
class ProgresoClienteAdmin(admin.ModelAdmin):
    list_display = ("cliente", "fecha", "peso_levantado_kg", "repeticiones")
