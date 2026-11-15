"""
Archivo: apps/clientes/admin.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Registro del modelo Cliente en el administrador de Django.
"""

from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombre", "apellidos", "telefono", "correo", "fecha_registro")
    search_fields = ("dni", "nombre", "apellidos", "correo")
