"""
Archivo: config/wsgi.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Punto de entrada WSGI para servidores web tradicionales.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()
