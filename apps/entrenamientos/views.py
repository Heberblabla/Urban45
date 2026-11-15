"""
Archivo: apps/entrenamientos/views.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Descripción: Vista para recomendar rutinas mediante reglas de negocio (programación
             lógica aplicada en Python) y visualizar el progreso físico de socios.
"""

from django.shortcuts import render

from apps.nucleo.datos_ejemplo import (
    obtener_lista_clientes,
    obtener_progreso_clientes,
)
from apps.nucleo.funciones_funcionales import calcular_promedio_peso
from apps.nucleo.reglas_negocio import (
    evaluar_rutina_recomendada,
    obtener_rutinas,
)


def vista_rutinas_entrenamiento(request):
    """
    Recomendador de rutinas basado en reglas de negocio (Guía, PDF p. 71)
    y tabla de seguimiento de progreso de los clientes (Guía, PDF p. 72).
    """
    lista_clientes = obtener_lista_clientes()
    catalogo_rutinas = obtener_rutinas()
    progresos = obtener_progreso_clientes()
    promedio_peso = calcular_promedio_peso(progresos)

    resultado_recomendacion = None
    datos_evaluacion = {
        "cliente_nombre": "Carlos Fernández",
        "objetivo": "masa_muscular",
        "condicion_fisica": "buena",
        "tiene_lesion": "no",
    }

    if request.method == "POST":
        datos_evaluacion = {
            "cliente_nombre": request.POST.get("cliente_nombre", "Carlos Fernández"),
            "objetivo": request.POST.get("objetivo", "masa_muscular"),
            "condicion_fisica": request.POST.get("condicion_fisica", "buena"),
            "tiene_lesion": request.POST.get("tiene_lesion", "no"),
        }
        resultado_recomendacion = evaluar_rutina_recomendada(
            datos_evaluacion["objetivo"],
            datos_evaluacion["condicion_fisica"],
            datos_evaluacion["tiene_lesion"],
        )

    contexto = {
        "pagina_activa": "entrenamientos",
        "lista_clientes": lista_clientes,
        "catalogo_rutinas": catalogo_rutinas,
        "progresos": progresos,
        "promedio_peso": promedio_peso,
        "datos_evaluacion": datos_evaluacion,
        "resultado_recomendacion": resultado_recomendacion,
    }
    return render(request, "rutinas_entrenamiento.html", contexto)
