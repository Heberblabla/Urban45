"""
Archivo: apps/clientes/views.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Descripción: Vistas del módulo de clientes, inicio de sesión y panel principal.
             Procesa los datos usando funciones funcionales y reglas de negocio
             compartidas desde apps.nucleo.
"""

from django.shortcuts import redirect, render

from apps.nucleo.datos_ejemplo import (
    obtener_lista_clientes,
    obtener_lista_pagos,
    obtener_planes_membresia,
    obtener_progreso_clientes,
)
from apps.nucleo.funciones_funcionales import (
    buscar_clientes,
    calcular_promedio_peso,
    calcular_total_pagos,
    filtrar_clientes_por_estado,
    filtrar_clientes_por_plan,
)
from apps.nucleo.reglas_negocio import (
    validar_datos_cliente,
    verificar_acceso_gimnasio,
)


def vista_login(request):
    """
    Pantalla de inicio de sesión de Urban 45 (Guía, PDF pp. 67 y 70).
    Funciona como vista de demostración para seleccionar el usuario y rol en sesión.
    """
    mensaje_demo = None

    if request.method == "POST":
        correo_ingresado = request.POST.get("correo", "").strip()
        rol_seleccionado = request.POST.get("rol_demo", "Administrador")

        if correo_ingresado:
            request.session["usuario_demo"] = correo_ingresado
            request.session["rol_demo"] = rol_seleccionado
            return redirect("panel_principal")
        else:
            mensaje_demo = "Por favor, ingresa un correo de ejemplo para continuar al panel principal."

    contexto = {
        "mensaje_demo": mensaje_demo,
    }
    return render(request, "login.html", contexto)


def vista_panel_principal(request):
    """
    Panel Principal (Dashboard) de Urban 45 (Guía, PDF p. 68).
    Calcula indicadores clave con filter(), map() y reduce().
    """
    lista_clientes = obtener_lista_clientes()
    lista_pagos = obtener_lista_pagos()
    lista_progresos = obtener_progreso_clientes()

    clientes_activos = filtrar_clientes_por_estado(lista_clientes, "Activa")
    clientes_por_vencer = filtrar_clientes_por_estado(lista_clientes, "Por Vencer")
    clientes_vencidos = filtrar_clientes_por_estado(lista_clientes, "Vencida")

    ingresos_recaudados = calcular_total_pagos(lista_pagos, estado_filtro="Pagado")
    pagos_pendientes = calcular_total_pagos(lista_pagos, estado_filtro="Pendiente")
    promedio_peso_kg = calcular_promedio_peso(lista_progresos)

    contexto = {
        "pagina_activa": "panel",
        "total_clientes": len(lista_clientes),
        "cantidad_activos": len(clientes_activos),
        "cantidad_por_vencer": len(clientes_por_vencer),
        "cantidad_vencidos": len(clientes_vencidos),
        "ingresos_recaudados": ingresos_recaudados,
        "pagos_pendientes": pagos_pendientes,
        "promedio_peso_kg": promedio_peso_kg,
        "ultimos_pagos": lista_pagos[:5],
    }
    return render(request, "panel_principal.html", contexto)


def vista_lista_clientes(request):
    """
    Listado general de clientes con buscador, filtros por plan/estado y
    evaluación automática de acceso permitido o denegado (Guía, PDF p. 69).
    """
    lista_clientes = obtener_lista_clientes()

    texto_busqueda = request.GET.get("buscar", "").strip()
    plan_filtro = request.GET.get("plan", "Todos")
    estado_filtro = request.GET.get("estado", "Todos")

    clientes_filtrados = buscar_clientes(lista_clientes, texto_busqueda)
    clientes_filtrados = filtrar_clientes_por_plan(clientes_filtrados, plan_filtro)
    clientes_filtrados = filtrar_clientes_por_estado(clientes_filtrados, estado_filtro)

    clientes_con_acceso = []
    for cliente in clientes_filtrados:
        datos_cliente = dict(cliente)
        datos_cliente["evaluacion_acceso"] = verificar_acceso_gimnasio(cliente)
        clientes_con_acceso.append(datos_cliente)

    contexto = {
        "pagina_activa": "clientes",
        "lista_clientes": clientes_con_acceso,
        "total_encontrados": len(clientes_con_acceso),
        "texto_busqueda": texto_busqueda,
        "plan_filtro": plan_filtro,
        "estado_filtro": estado_filtro,
    }
    return render(request, "lista_clientes.html", contexto)


def vista_registrar_cliente(request):
    """
    Formulario de inscripción de nuevos clientes con validación de reglas de negocio
    (DNI único, correo válido, teléfono de 9 dígitos y campos obligatorios).
    """
    planes = obtener_planes_membresia()
    lista_clientes = obtener_lista_clientes()

    errores_validacion = []
    cliente_validado_demo = None
    datos_formulario = {
        "nombre": "",
        "apellidos": "",
        "dni": "",
        "telefono": "",
        "correo": "",
        "tipo_membresia": "Premium",
        "objetivo": "Aumento de masa muscular",
    }

    if request.method == "POST":
        datos_formulario = {
            "nombre": request.POST.get("nombre", "").strip(),
            "apellidos": request.POST.get("apellidos", "").strip(),
            "dni": request.POST.get("dni", "").strip(),
            "telefono": request.POST.get("telefono", "").strip(),
            "correo": request.POST.get("correo", "").strip(),
            "tipo_membresia": request.POST.get("tipo_membresia", "Premium"),
            "objetivo": request.POST.get("objetivo", "Aumento de masa muscular"),
        }

        errores_validacion = validar_datos_cliente(datos_formulario, lista_clientes)

        if not errores_validacion:
            nuevo_cliente_temp = {
                "nombre": datos_formulario["nombre"],
                "apellidos": datos_formulario["apellidos"],
                "dni": datos_formulario["dni"],
                "telefono": datos_formulario["telefono"],
                "correo": datos_formulario["correo"],
                "tipo_membresia": datos_formulario["tipo_membresia"],
                "objetivo": datos_formulario["objetivo"],
                "estado_membresia": "Activa",
                "dias_restantes": 30,
                "pago_al_dia": True,
            }
            nuevo_cliente_temp["evaluacion_acceso"] = verificar_acceso_gimnasio(nuevo_cliente_temp)
            cliente_validado_demo = nuevo_cliente_temp

    contexto = {
        "pagina_activa": "registrar_cliente",
        "planes": planes,
        "datos_formulario": datos_formulario,
        "errores_validacion": errores_validacion,
        "cliente_validado_demo": cliente_validado_demo,
    }
    return render(request, "registrar_cliente.html", contexto)
