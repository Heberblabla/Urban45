"""
Archivo: apps/entrenamientos/urls.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Rutas URL del módulo de entrenamientos y progreso físico.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("entrenamientos/", views.vista_rutinas_entrenamiento, name="rutinas_entrenamiento"),
]
