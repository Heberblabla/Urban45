"""
Archivo: apps/membresias/urls.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Rutas URL del módulo de membresías y pagos.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("membresias/", views.vista_gestion_membresias, name="gestion_membresias"),
    path("pagos/", views.vista_gestion_pagos, name="gestion_pagos"),
]
