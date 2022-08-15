from django.contrib import admin

from .models import(
   Escolaridade,
   Experiencia,
   MinhaIscricao,
   PretencaoSalarial,
   DadosPessoais
)

admin.site.register(Escolaridade)
admin.site.register(Experiencia)
admin.site.register(MinhaIscricao)
admin.site.register(PretencaoSalarial)
admin.site.register(DadosPessoais)