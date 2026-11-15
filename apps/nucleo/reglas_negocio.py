"""
Archivo: apps/nucleo/reglas_negocio.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Autor: Equipo de Desarrollo Urban 45
Descripción: Reglas de negocio inspiradas en los principios de la Programación
             Lógica estudiada en el curso (evaluación de hechos y condiciones
             para tomar decisiones sobre vigencias, accesos y rutinas).
"""


def membresia_esta_vigente(estado_membresia, dias_restantes):
    """
    Evalúa si una membresía se considera vigente.
    Condición lógica: El estado no debe ser 'Vencida' y debe tener más de 0 días restantes.
    """
    return estado_membresia in ("Activa", "Por Vencer") and dias_restantes > 0


def verificar_acceso_gimnasio(cliente):
    """
    Evalúa las condiciones que debe cumplir un cliente para ingresar al gimnasio:
    1. Su membresía debe estar vigente (Activa o Por Vencer con días > 0).
    2. Su pago mensual debe estar al día.

    Devuelve un diccionario indicando si puede pasar y el motivo.
    """
    tiene_vigencia = membresia_esta_vigente(
        cliente["estado_membresia"],
        cliente["dias_restantes"]
    )
    pago_al_dia = cliente["pago_al_dia"]

    # Ambas condiciones deben cumplirse simultáneamente (conjunción lógica AND)
    if tiene_vigencia and pago_al_dia:
        return {
            "permitido": True,
            "mensaje": "Acceso permitido",
            "color": "success"
        }

    # Si alguna condición falla, indicamos la razón específica
    if not tiene_vigencia:
        return {
            "permitido": False,
            "mensaje": "Membresía vencida",
            "color": "danger"
        }

    return {
        "permitido": False,
        "mensaje": "Pago pendiente",
        "color": "warning"
    }


def obtener_rutinas():
    """Devuelve el catálogo base de rutinas disponibles en Urban 45."""
    rutinas = [
        {
            "nombre": "Programa de Fuerza e Hipertrofia",
            "frecuencia": "4 a 5 días por semana",
            "enfoque": "Pesas libres, máquinas de musculación y sobrecarga progresiva.",
            "entrenador": "Claudio Torres",
        },
        {
            "nombre": "Programa de Acondicionamiento Inicial",
            "frecuencia": "3 días por semana",
            "enfoque": "Adaptación muscular, técnica de ejercicios básicos y cardio moderado.",
            "entrenador": "Claudio Torres",
        },
        {
            "nombre": "Circuito Funcional Quema Grasa (Urban 45)",
            "frecuencia": "4 días por semana",
            "enfoque": "Circuitos metabólicos, intervalos de intensidad y resistencia.",
            "entrenador": "Elena Gómez",
        },
        {
            "nombre": "Programa de Movilidad y Salud Articular",
            "frecuencia": "2 a 3 días por semana",
            "enfoque": "Ejercicios de bajo impacto, fortalecimiento guiado y flexibilidad.",
            "entrenador": "Elena Gómez",
        },
    ]
    return rutinas


def evaluar_rutina_recomendada(objetivo, condicion_fisica, tiene_lesion):
    """
    Evalúa los datos del cliente (hechos de entrada) y devuelve la rutina más
    adecuada según las reglas de entrenamiento del gimnasio (Guía, PDF p. 71).
    """
    # Regla 1: Si el cliente reporta lesión o molestia articular, priorizamos salud articular
    if tiene_lesion == "si":
        return {
            "rutina": "Programa de Movilidad y Salud Articular",
            "frecuencia": "2 a 3 días por semana",
            "entrenador": "Elena Gómez",
            "explicacion": "Se prioriza el cuidado articular y ejercicios sin impacto por precaución médica.",
        }

    # Regla 2: Objetivo de masa muscular con buena condición física
    if objetivo == "masa_muscular" and condicion_fisica in ("buena", "intermedia"):
        return {
            "rutina": "Programa de Fuerza e Hipertrofia",
            "frecuencia": "4 a 5 días por semana",
            "entrenador": "Claudio Torres",
            "explicacion": "El cliente cuenta con base física para trabajar cargas progresivas de hipertrofia.",
        }

    # Regla 3: Objetivo de masa muscular pero recién inicia (condición inicial)
    if objetivo == "masa_muscular" and condicion_fisica == "inicial":
        return {
            "rutina": "Programa de Acondicionamiento Inicial",
            "frecuencia": "3 días por semana",
            "entrenador": "Claudio Torres",
            "explicacion": "Antes de levantar cargas altas, requiere dominar la técnica y adaptar tendones.",
        }

    # Regla 4: Objetivo de bajar de peso o mejorar resistencia
    if objetivo in ("perdida_peso", "resistencia") and condicion_fisica in ("buena", "intermedia"):
        return {
            "rutina": "Circuito Funcional Quema Grasa (Urban 45)",
            "frecuencia": "4 días por semana",
            "entrenador": "Elena Gómez",
            "explicacion": "Combina trabajo funcional y cardiovascular para maximizar el gasto calórico.",
        }

    # Regla por defecto para cualquier otro caso inicial
    return {
        "rutina": "Programa de Acondicionamiento Inicial",
        "frecuencia": "3 días por semana",
        "entrenador": "Claudio Torres",
        "explicacion": "Plan equilibrado ideal para construir hábito y mejorar la capacidad general.",
    }


def validar_datos_cliente(datos, lista_clientes_actual):
    """
    Verifica que los campos enviados en el formulario de registro de cliente
    cumplan con las reglas obligatorias antes de ser aceptados (RF1 y RF4, Guía p. 26).
    Devuelve una lista de errores encontrados (vacía si todo es válido).
    """
    errores = []

    nombre = datos.get("nombre", "").strip()
    apellidos = datos.get("apellidos", "").strip()
    dni = datos.get("dni", "").strip()
    telefono = datos.get("telefono", "").strip()
    correo = datos.get("correo", "").strip()

    if len(nombre) < 2:
        errores.append("El nombre del cliente es obligatorio y debe tener al menos 2 letras.")

    if len(apellidos) < 2:
        errores.append("Los apellidos del cliente son obligatorios.")

    if not dni.isdigit() or len(dni) != 8:
        errores.append("El DNI debe contener exactamente 8 dígitos numéricos.")

    # Regla RF4 (Guía, PDF p. 26): Verificar si el cliente ya está registrado
    for cliente_existente in lista_clientes_actual:
        if cliente_existente["dni"] == dni:
            errores.append(f"Ya existe un cliente registrado con el DNI {dni}.")
            break

    if not telefono.isdigit() or len(telefono) < 7:
        errores.append("El número de teléfono debe contener solo dígitos válidos.")

    if "@" not in correo or "." not in correo:
        errores.append("Debe ingresar un correo electrónico con formato válido.")

    return errores
