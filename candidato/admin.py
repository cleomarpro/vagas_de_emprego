from django.contrib import admin

from .models import(
   Escolaridade,
   Experiencia
)

admin.site.register(Escolaridade)
admin.site.register(Experiencia)
