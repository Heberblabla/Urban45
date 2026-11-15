#!/usr/bin/env python
"""
Archivo: manage.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Curso: Lenguajes de Programación - UTP
Descripción: Herramienta principal de Django para ejecutar el servidor web,
             generar migraciones y administrar el proyecto desde la terminal.
"""
import os
import sys


def main():
    """Función principal que ejecuta los comandos administrativos de Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Verifica que esté instalado y "
            "que tu entorno virtual esté activado."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
