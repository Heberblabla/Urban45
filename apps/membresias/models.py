"""
Archivo: apps/membresias/models.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Descripción: Modelos PlanMembresia, Membresia y Pago (Programación Orientada
             a Objetos) con relación hacia clientes.Cliente.
"""

from django.db import models


class PlanMembresia(models.Model):
    """Representa un tipo de plan que ofrece el gimnasio (Básico, Standard o Premium)."""

    nombre_plan = models.CharField(max_length=50, unique=True)
    precio_mensual = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_dias = models.PositiveIntegerField(default=30)
    descripcion = models.TextField(blank=True)

    class Meta:
        db_table = "plan_membresia"
        verbose_name = "Plan de Membresía"
        verbose_name_plural = "Planes de Membresía"

    def calcular_precio_con_descuento(self, porcentaje_descuento):
        """Calcula el precio aplicando un descuento promocional."""
        descuento = float(self.precio_mensual) * (porcentaje_descuento / 100)
        return round(float(self.precio_mensual) - descuento, 2)

    def __str__(self):
        return f"Plan {self.nombre_plan} (S/. {self.precio_mensual})"


class Membresia(models.Model):
    """Representa la suscripción contratada por un cliente en un plan específico."""

    ESTADOS = [
        ("Activa", "Activa"),
        ("Por Vencer", "Por Vencer"),
        ("Vencida", "Vencida"),
    ]

    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
        related_name="membresias",
    )
    plan = models.ForeignKey(
        PlanMembresia,
        on_delete=models.PROTECT,
        related_name="membresias",
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default="Activa")

    class Meta:
        db_table = "membresia"
        verbose_name = "Membresía"
        verbose_name_plural = "Membresías"

    def esta_activa(self):
        """Devuelve True si la membresía permite el ingreso al gimnasio."""
        return self.estado in ("Activa", "Por Vencer")

    def __str__(self):
        return f"{self.cliente.obtener_nombre_completo()} - {self.plan.nombre_plan} ({self.estado})"


class Pago(models.Model):
    """Representa un comprobante o recibo de pago emitido al cliente."""

    ESTADOS_PAGO = [
        ("Pagado", "Pagado"),
        ("Pendiente", "Pendiente"),
    ]

    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
        related_name="pagos",
    )
    membresia = models.ForeignKey(
        Membresia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pagos",
    )
    concepto = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_pago = models.DateField()
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default="Pagado")

    class Meta:
        db_table = "pago"
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"Recibo #{self.id} - {self.cliente.obtener_nombre_completo()} (S/. {self.monto})"
