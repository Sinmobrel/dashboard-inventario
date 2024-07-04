from django.urls import path
from api.core.apiviews import Persona, ListPersona, Empresa, ListEmpresa, GrupoTrabajo, ListGrupoTrabajo , Personal, ListPersonal, Producto, ListProducto
urlpatterns = [
    
    path('get/Persona/<persona_id>/', Persona.as_view()),
    path('post/Persona/', Persona.as_view()),
    path('delete/Persona/<persona_id>/', Persona.as_view()),
    path('get/list/Persona/', ListPersona.as_view()),

# mio
# <- --------------------------------------------------------------------------- ->

    path('post/Empresa/', Empresa.as_view()),
    path('get/Empresa/<empresa_id>', Empresa.as_view()),
    path('delete/Empresa/<empresa_id>', Empresa.as_view()),
    path('get/list/Empresa/', ListEmpresa.as_view()),

# <- --------------------------------------------------------------------------- ->

    path('post/GrupoTrabajo/', GrupoTrabajo.as_view()),
    path('get/GrupoTrabajo/<grupoTrabajo_id>', GrupoTrabajo.as_view()),
    path('delete/GrupoTrabajo/<grupoTrabajo_id>', GrupoTrabajo.as_view()),
    path('get/list/GrupoTrabajo/', ListGrupoTrabajo.as_view()),

# <- --------------------------------------------------------------------------- ->

    path('post/Personal/', Personal.as_view()),
    path('get/Personal/<personal_id>', Personal.as_view()),
    path('delete/Personal/<personal_id>', Personal.as_view()),
    path('get/list/Personal/', ListPersonal.as_view()),

# <- --------------------------------------------------------------------------- ->

    path('post/Producto/', Producto.as_view()),
    path('get/Producto/<producto_id>', Producto.as_view()),
    path('delete/Producto/<producto_id>', Producto.as_view()),
    path('get/list/Producto/', ListProducto.as_view()),


]
