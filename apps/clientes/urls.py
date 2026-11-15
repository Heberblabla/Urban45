"""
Archivo: apps/clientes/urls.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Rutas URL del módulo de clientes, login y panel principal.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.vista_panel_principal, name="panel_principal"),
    path("login/", views.vista_login, name="login"),
    path("clientes/", views.vista_lista_clientes, name="lista_clientes"),
    path("clientes/registrar/", views.vista_registrar_cliente, name="registrar_cliente"),
]
