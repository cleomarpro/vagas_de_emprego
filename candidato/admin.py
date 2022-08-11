from django.contrib import admin

from .models import(
   Escolaridade,
   Experiencia,
   MinhaIscricao
)

admin.site.register(Escolaridade)
admin.site.register(Experiencia)
admin.site.register(MinhaIscricao)
