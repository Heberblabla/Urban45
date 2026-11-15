"""
Archivo: apps/nucleo/apps.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Registro de la aplicación nucleo dentro del paquete apps/.
"""

from django.apps import AppConfig


class NucleoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.nucleo"
    verbose_name = "Núcleo Compartido Urban 45"
