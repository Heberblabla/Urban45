"""
Archivo: apps/membresias/views.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Descripción: Vistas del módulo de membresías y pagos. Demuestra el uso de
             map(), filter(), reduce() y recursividad en escenarios reales del gimnasio.
"""

from django.shortcuts import render

from apps.nucleo.datos_ejemplo import (
    obtener_lista_clientes,
    obtener_lista_pagos,
    obtener_planes_membresia,
)
from apps.nucleo.funciones_funcionales import (
    aplicar_descuento_a_planes,
    calcular_pago_acumulado_recursivo,
    calcular_total_pagos,
)


def vista_gestion_membresias(request):
    """
    Muestra el catálogo de planes de membresía, la calculadora funcional de
    descuentos con map() y el simulador recursivo de pagos por meses.
    """
    planes_base = obtener_planes_membresia()
    lista_clientes = obtener_lista_clientes()

    try:
        porcentaje_descuento = int(request.GET.get("descuento", 0))
        if porcentaje_descuento not in (0, 10, 15, 20):
            porcentaje_descuento = 0
    except ValueError:
        porcentaje_descuento = 0

    planes_mostrados = aplicar_descuento_a_planes(planes_base, porcentaje_descuento)

    plan_simulado_nombre = request.GET.get("plan_simulado", "Premium")
    try:
        meses_simulados = int(request.GET.get("meses", 3))
        if meses_simulados < 1 or meses_simulados > 12:
            meses_simulados = 3
    except ValueError:
        meses_simulados = 3

    precio_base_elegido = 200.00
    for plan in planes_base:
        if plan["nombre"] == plan_simulado_nombre:
            precio_base_elegido = plan["precio"]
            break

    costo_recursivo_total = calcular_pago_acumulado_recursivo(meses_simulados, precio_base_elegido)
    costo_sin_beneficio = round(precio_base_elegido * meses_simulados, 2)
    ahorro_fidelidad = round(costo_sin_beneficio - costo_recursivo_total, 2)

    contexto = {
        "pagina_activa": "membresias",
        "planes": planes_mostrados,
        "porcentaje_descuento": porcentaje_descuento,
        "plan_simulado_nombre": plan_simulado_nombre,
        "meses_simulados": meses_simulados,
        "precio_base_elegido": precio_base_elegido,
        "costo_recursivo_total": costo_recursivo_total,
        "costo_sin_beneficio": costo_sin_beneficio,
        "ahorro_fidelidad": ahorro_fidelidad,
        "lista_clientes": lista_clientes,
    }
    return render(request, "gestion_membresias.html", contexto)


def vista_gestion_pagos(request):
    """
    Pantalla de Gestión de Pagos y Facturación (inspirada en Guía PDF p. 73).
    Incluye validación de registro de pago (modo demostración), vista previa
    de reporte de facturación y tabla filtrable de facturas con reduce().
    """
    lista_clientes = obtener_lista_clientes()
    lista_pagos = obtener_lista_pagos()

    estado_filtro = request.GET.get("estado", "Todos")
    if estado_filtro in ("Pagado", "Pendiente"):
        pagos_filtrados = list(filter(lambda p: p["estado"] == estado_filtro, lista_pagos))
    else:
        estado_filtro = "Todos"
        pagos_filtrados = lista_pagos

    total_recaudado = calcular_total_pagos(lista_pagos, estado_filtro="Pagado")
    total_pendiente = calcular_total_pagos(lista_pagos, estado_filtro="Pendiente")
    total_general = calcular_total_pagos(lista_pagos, estado_filtro="Todos")

    errores_pago = []
    pago_demo_validado = None
    reporte_demo = None
    datos_pago = {
        "cliente_nombre": "David Lachira",
        "plan": "Premium",
        "monto": "200.00",
        "fecha": "2026-11-10",
    }

    if request.method == "POST":
        accion = request.POST.get("accion", "")

        if accion == "registrar_pago":
            datos_pago = {
                "cliente_nombre": request.POST.get("cliente_nombre", "").strip(),
                "plan": request.POST.get("plan", "Premium").strip(),
                "monto": request.POST.get("monto", "").strip(),
                "fecha": request.POST.get("fecha", "").strip(),
            }

            if not datos_pago["cliente_nombre"]:
                errores_pago.append("Debe seleccionar un cliente válido.")
            try:
                monto_numero = float(datos_pago["monto"])
                if monto_numero <= 0:
                    errores_pago.append("El monto del pago debe ser mayor a S/. 0.00.")
            except ValueError:
                errores_pago.append("El monto ingresado debe ser un número válido.")
                monto_numero = 0.0
            if not datos_pago["fecha"]:
                errores_pago.append("Debe indicar una fecha de pago.")

            if not errores_pago:
                pago_demo_validado = {
                    "id_factura_vista": "7141",
                    "cliente": datos_pago["cliente_nombre"],
                    "plan": datos_pago["plan"],
                    "monto": round(monto_numero, 2),
                    "fecha": datos_pago["fecha"],
                    "estado": "Pagado",
                }

        elif accion == "generar_reporte":
            reporte_demo = {
                "cantidad_facturas": len(pagos_filtrados),
                "filtro_aplicado": estado_filtro,
                "total_recaudado": total_recaudado,
                "total_pendiente": total_pendiente,
                "total_acumulado": round(sum(p["monto"] for p in pagos_filtrados), 2),
            }

    contexto = {
        "pagina_activa": "pagos",
        "lista_clientes": lista_clientes,
        "pagos_filtrados": pagos_filtrados,
        "estado_filtro": estado_filtro,
        "total_recaudado": total_recaudado,
        "total_pendiente": total_pendiente,
        "total_general": total_general,
        "datos_pago": datos_pago,
        "errores_pago": errores_pago,
        "pago_demo_validado": pago_demo_validado,
        "reporte_demo": reporte_demo,
    }
    return render(request, "gestion_pagos.html", contexto)
