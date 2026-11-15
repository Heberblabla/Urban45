"""
Archivo: apps/nucleo/funciones_funcionales.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Autor: Equipo de Desarrollo Urban 45
Descripción: Aplicación práctica de Programación Funcional (funciones puras,
             map, filter y reduce) y Recursividad para procesar los datos
             de clientes, planes, pagos y entrenamientos del gimnasio.
"""

from functools import reduce


# ==============================================================================
# 1. FUNCIONES PURAS Y TRANSFORMACIÓN DE DATOS (PROGRAMACIÓN FUNCIONAL)
# ==============================================================================

def calcular_descuento(precio, porcentaje):
    """
    Función pura: recibe un precio y un porcentaje de descuento,
    y devuelve el precio final sin modificar ninguna variable externa.
    """
    descuento = precio * porcentaje / 100
    return round(precio - descuento, 2)


def filtrar_clientes_por_estado(lista_clientes, estado_buscado):
    """
    Utiliza filter() para obtener únicamente los clientes que tienen
    el estado de membresía indicado ('Activa', 'Por Vencer' o 'Vencida').
    """
    if not estado_buscado or estado_buscado == "Todos":
        return lista_clientes

    clientes_filtrados = filter(
        lambda cliente: cliente["estado_membresia"] == estado_buscado,
        lista_clientes
    )
    return list(clientes_filtrados)


def filtrar_clientes_por_plan(lista_clientes, nombre_plan):
    """
    Utiliza filter() para obtener los clientes inscritos en un plan
    específico ('Básico', 'Standard' o 'Premium').
    """
    if not nombre_plan or nombre_plan == "Todos":
        return lista_clientes

    clientes_filtrados = filter(
        lambda cliente: cliente["tipo_membresia"] == nombre_plan,
        lista_clientes
    )
    return list(clientes_filtrados)


def buscar_clientes(lista_clientes, texto_busqueda):
    """
    Utiliza filter() para buscar clientes cuyo nombre, apellido o DNI
    coincida con el texto escrito en el buscador.
    """
    if not texto_busqueda:
        return lista_clientes

    texto = texto_busqueda.strip().lower()

    def coincide_busqueda(cliente):
        nombre_completo = f"{cliente['nombre']} {cliente['apellidos']}".lower()
        return texto in nombre_completo or texto in cliente["dni"]

    return list(filter(coincide_busqueda, lista_clientes))


def aplicar_descuento_a_planes(lista_planes, porcentaje):
    """
    Utiliza map() para crear una nueva lista de planes con el precio
    promocional calculado, sin alterar los planes originales.
    """
    def transformar_plan(plan):
        nuevo_plan = dict(plan)
        nuevo_plan["precio_con_descuento"] = calcular_descuento(plan["precio"], porcentaje)
        nuevo_plan["ahorro"] = round(plan["precio"] - nuevo_plan["precio_con_descuento"], 2)
        return nuevo_plan

    return list(map(transformar_plan, lista_planes))


def calcular_total_pagos(lista_pagos, estado_filtro="Pagado"):
    """
    Combina filter(), map() y reduce() para sumar el dinero recaudado
    en los pagos que cumplen con el estado indicado.
    """
    # 1. Filtramos los pagos según su estado (por ejemplo, solo 'Pagado')
    pagos_validos = list(filter(lambda p: p["estado"] == estado_filtro, lista_pagos))

    if not pagos_validos:
        return 0.0

    # 2. Extraemos únicamente los montos numéricos con map()
    lista_montos = list(map(lambda p: p["monto"], pagos_validos))

    # 3. Sumamos todos los montos usando reduce()
    suma_total = reduce(lambda acumulado, monto: acumulado + monto, lista_montos, 0.0)
    return round(suma_total, 2)


def calcular_promedio_peso(lista_progresos):
    """
    Utiliza map() y reduce() para calcular el promedio de peso levantado (kg)
    en las sesiones de entrenamiento registradas.
    """
    if not lista_progresos:
        return 0.0

    pesos = list(map(lambda reg: reg["peso_levantado_kg"], lista_progresos))
    suma_pesos = reduce(lambda a, b: a + b, pesos, 0)
    return round(suma_pesos / len(pesos), 1)


# ==============================================================================
# 2. APLICACIÓN DE RECURSIVIDAD
# ==============================================================================

def calcular_pago_acumulado_recursivo(meses, precio_mensual):
    """
    Calcula el costo total acumulado al contratar varios meses seguidos,
    aplicando un beneficio por fidelidad: a partir del segundo mes,
    cada mes adicional tiene S/. 5.00 de descuento respecto al precio base.

    Parámetros:
        meses (int): Cantidad de meses a contratar (1 a 12).
        precio_mensual (float): Precio normal de un mes del plan.
    """
    # Caso base: Si solo se contrata 1 mes (o menos), se paga el precio mensual normal.
    if meses <= 1:
        return round(precio_mensual, 2)

    # Caso recursivo: Calculamos el costo del mes actual con beneficio de S/. 5.00
    # y le sumamos el resultado de llamar a la misma función para (meses - 1).
    costo_mes_actual = max(precio_mensual - 5.0, 0.0)
    return round(costo_mes_actual + calcular_pago_acumulado_recursivo(meses - 1, precio_mensual), 2)
