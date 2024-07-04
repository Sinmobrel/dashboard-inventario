from django.contrib import admin
from apps.core.models import Persona, Empresa, GrupoTrabajo, Personal, Producto

admin.site.register(Persona)

#mio
# <- ---------------------------------------------------------------------------------- ->

admin.site.register(Empresa)
admin.site.register(GrupoTrabajo)
admin.site.register(Personal)
admin.site.register(Producto)