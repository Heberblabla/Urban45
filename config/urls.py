"""
Archivo: config/urls.py
Proyecto: Sistema Web Urban 45 - Gimnasio Smart
Descripción: Enrutador principal del sistema. Conecta el panel administrativo de
             Django y delega las pantallas web a cada aplicación en apps/.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.clientes.urls")),
    path("", include("apps.membresias.urls")),
    path("", include("apps.entrenamientos.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
