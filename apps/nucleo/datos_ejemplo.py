"""
Archivo: apps/nucleo/datos_ejemplo.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Autor: Equipo de Desarrollo Urban 45
Descripción: Datos de ejemplo basados en las pantallas de la guía de Urban 45
             (Guía, PDF pp. 69–73). Permiten mostrar y probar el frontend
             mientras se completa la conexión definitiva con PostgreSQL.
"""


def obtener_planes_membresia():
    """Devuelve la lista de planes disponibles en el gimnasio Urban 45."""
    planes = [
        {
            "codigo": "BASICO",
            "nombre": "Básico",
            "precio": 90.00,
            "duracion_dias": 30,
            "beneficios": "Acceso al área de musculación y cardio en horario regular.",
            "color_etiqueta": "secondary",
        },
        {
            "codigo": "STANDARD",
            "nombre": "Standard",
            "precio": 140.00,
            "duracion_dias": 30,
            "beneficios": "Musculación, zona de cardio y acceso a clases grupales.",
            "color_etiqueta": "primary",
        },
        {
            "codigo": "PREMIUM",
            "nombre": "Premium",
            "precio": 200.00,
            "duracion_dias": 30,
            "beneficios": "Acceso total, área funcional, seguimiento de progreso y entrenador.",
            "color_etiqueta": "warning",
        },
    ]
    return planes


def obtener_lista_clientes():
    """
    Devuelve la lista de clientes registrados de ejemplo.
    Los nombres y correos provienen de la tabla de usuarios de la guía (PDF p. 69).
    """
    lista_clientes = [
        {
            "id": 1,
            "dni": "71234501",
            "nombre": "David",
            "apellidos": "Lachira",
            "telefono": "987654321",
            "correo": "da.lachira@email.com",
            "tipo_membresia": "Premium",
            "estado_membresia": "Activa",
            "dias_restantes": 22,
            "pago_al_dia": True,
            "objetivo": "Aumento de masa muscular",
        },
        {
            "id": 2,
            "dni": "71234502",
            "nombre": "Odalis",
            "apellidos": "Domínguez",
            "telefono": "912345678",
            "correo": "odalis@email.com",
            "tipo_membresia": "Básico",
            "estado_membresia": "Activa",
            "dias_restantes": 15,
            "pago_al_dia": True,
            "objetivo": "Resistencia y tonificación",
        },
        {
            "id": 3,
            "dni": "71234503",
            "nombre": "Jorge",
            "apellidos": "Suárez",
            "telefono": "961234567",
            "correo": "jorge.suarez@email.com",
            "tipo_membresia": "Premium",
            "estado_membresia": "Por Vencer",
            "dias_restantes": 4,
            "pago_al_dia": True,
            "objetivo": "Fuerza máxima",
        },
        {
            "id": 4,
            "dni": "71234504",
            "nombre": "Yarlequé",
            "apellidos": "Timaná",
            "telefono": "930123456",
            "correo": "yarleque@email.com",
            "tipo_membresia": "Básico",
            "estado_membresia": "Vencida",
            "dias_restantes": 0,
            "pago_al_dia": False,
            "objetivo": "Pérdida de peso",
        },
        {
            "id": 5,
            "dni": "71234505",
            "nombre": "María",
            "apellidos": "López",
            "telefono": "915678234",
            "correo": "maria.lopez@email.com",
            "tipo_membresia": "Standard",
            "estado_membresia": "Activa",
            "dias_restantes": 18,
            "pago_al_dia": True,
            "objetivo": "Clases funcionales y cardio",
        },
        {
            "id": 6,
            "dni": "71234506",
            "nombre": "Carlos",
            "apellidos": "Fernández",
            "telefono": "987123654",
            "correo": "carlos.fernandez@email.com",
            "tipo_membresia": "Premium",
            "estado_membresia": "Activa",
            "dias_restantes": 27,
            "pago_al_dia": True,
            "objetivo": "Aumento de masa muscular",
        },
        {
            "id": 7,
            "dni": "71234507",
            "nombre": "Lucía",
            "apellidos": "Martínez",
            "telefono": "951234789",
            "correo": "lucia.martinez@email.com",
            "tipo_membresia": "Básico",
            "estado_membresia": "Por Vencer",
            "dias_restantes": 3,
            "pago_al_dia": True,
            "objetivo": "Salud general",
        },
        {
            "id": 8,
            "dni": "71234508",
            "nombre": "Pedro",
            "apellidos": "García",
            "telefono": "921345678",
            "correo": "pedro.garcia@email.com",
            "tipo_membresia": "Standard",
            "estado_membresia": "Vencida",
            "dias_restantes": 0,
            "pago_al_dia": False,
            "objetivo": "Pérdida de peso",
        },
        {
            "id": 9,
            "dni": "71234509",
            "nombre": "Elena",
            "apellidos": "Torres",
            "telefono": "912345987",
            "correo": "elena.torres@email.com",
            "tipo_membresia": "Premium",
            "estado_membresia": "Activa",
            "dias_restantes": 25,
            "pago_al_dia": True,
            "objetivo": "Fuerza y resistencia",
        },
    ]
    return lista_clientes


def obtener_progreso_clientes():
    """
    Devuelve los registros de progreso físico de ejemplo.
    Referencia: Pantalla 'Progreso de los Clientes' (Guía, PDF p. 72).
    """
    progresos = [
        {
            "id": 1,
            "cliente": "Odalis Domínguez",
            "fecha": "2026-10-25",
            "peso_levantado_kg": 50,
            "repeticiones": 12,
            "comentario": "Buen progreso esta semana",
        },
        {
            "id": 2,
            "cliente": "Carlos Fernández",
            "fecha": "2026-10-26",
            "peso_levantado_kg": 70,
            "repeticiones": 10,
            "comentario": "Mejorar técnica en press de banca",
        },
        {
            "id": 3,
            "cliente": "Elena Torres",
            "fecha": "2026-10-28",
            "peso_levantado_kg": 30,
            "repeticiones": 15,
            "comentario": "Incrementar peso la próxima sesión",
        },
        {
            "id": 4,
            "cliente": "David Lachira",
            "fecha": "2026-11-01",
            "peso_levantado_kg": 80,
            "repeticiones": 8,
            "comentario": "Excelente control de carga en sentadilla",
        },
    ]
    return progresos


def obtener_lista_pagos():
    """
    Devuelve los registros de pagos de ejemplo para calcular estadísticas.
    Referencia: Pantalla 'Gestión de Pagos' (Guía, PDF p. 73).
    """
    pagos = [
        {"id_factura": "7133", "cliente": "David Lachira", "plan": "Premium", "monto": 200.00, "fecha": "2026-10-15", "estado": "Pagado"},
        {"id_factura": "7134", "cliente": "Odalis Domínguez", "plan": "Básico", "monto": 90.00, "fecha": "2026-10-18", "estado": "Pagado"},
        {"id_factura": "7135", "cliente": "Jorge Suárez", "plan": "Premium", "monto": 200.00, "fecha": "2026-10-20", "estado": "Pagado"},
        {"id_factura": "7136", "cliente": "María López", "plan": "Standard", "monto": 140.00, "fecha": "2026-10-22", "estado": "Pagado"},
        {"id_factura": "7137", "cliente": "Carlos Fernández", "plan": "Premium", "monto": 200.00, "fecha": "2026-10-25", "estado": "Pagado"},
        {"id_factura": "7138", "cliente": "Elena Torres", "plan": "Premium", "monto": 200.00, "fecha": "2026-10-28", "estado": "Pagado"},
        {"id_factura": "7139", "cliente": "Yarlequé Timaná", "plan": "Básico", "monto": 90.00, "fecha": "2026-11-01", "estado": "Pendiente"},
        {"id_factura": "7140", "cliente": "Pedro García", "plan": "Standard", "monto": 140.00, "fecha": "2026-11-02", "estado": "Pendiente"},
    ]
    return pagos
