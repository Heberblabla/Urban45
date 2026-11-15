"""
Archivo: apps/membresias/apps.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Configuración de la aplicación membresias.
"""

from django.apps import AppConfig


class MembresiasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.membresias"
    verbose_name = "Gestión de Membresías y Pagos"
