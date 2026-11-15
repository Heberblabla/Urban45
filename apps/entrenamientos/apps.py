"""
Archivo: apps/entrenamientos/apps.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Configuración de la aplicación entrenamientos.
"""

from django.apps import AppConfig


class EntrenamientosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.entrenamientos"
    verbose_name = "Planes de Entrenamiento y Progreso"
