from django.shortcuts import render
from apps.core.models import Persona, Empresa, GrupoTrabajo, Personal, Producto

def index(request):
    template_name = "index.html"
    context = {} 
    return render(request, template_name, context)