"""
Archivo: apps/membresias/admin.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Registro de modelos del módulo de membresías y pagos.
"""

from django.contrib import admin
from .models import Membresia, Pago, PlanMembresia


@admin.register(PlanMembresia)
class PlanMembresiaAdmin(admin.ModelAdmin):
    list_display = ("nombre_plan", "precio_mensual", "duracion_dias")


@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "plan", "fecha_inicio", "fecha_fin", "estado")
    list_filter = ("estado", "plan")


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "concepto", "monto", "fecha_pago", "estado_pago")
    list_filter = ("estado_pago",)
