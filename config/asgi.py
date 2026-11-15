"""
Archivo: config/asgi.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Punto de entrada ASGI para servidores asíncronos en producción.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_asgi_application()
