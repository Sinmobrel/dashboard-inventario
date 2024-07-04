from apps.core.models import Persona, Empresa, GrupoTrabajo, Personal, Producto
from apps.core.serializers import PersonaSerializer, EmpresaSerializer, GrupoTrabajoSerializer, PersonalSerializer, ProductoSerializer
from django.http import Http404


def get_name(i=None):
    if i is not None:
        try:
            i = int(i)
            p = Persona.objects.get(id=i)
            return PersonaSerializer(p).data
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404

def traer_personas(request):
    p = Persona.objects.all()
    return PersonaSerializer(p, context={"request": request}, many=True).data

def guardar_persona(**kwargs):
    if 'nombre' in kwargs and kwargs.get('nombre') != "" and type(kwargs.get('nombre')) == str:
        p = Persona.objects.create(name = kwargs.get('nombre'))
        p.f_nacimiento = kwargs.get('f_nacimiento') if 'f_nacimiento' in kwargs else None
        p.ciudad = kwargs.get('ciudad') if 'ciudad' in kwargs else None
        p.avatar = kwargs.get('avatar') if 'avatar' in kwargs else None
        p.save()
        return True
    else:
        return False
    
def borrar_persona(i=None):
    if i is not None:
        try:
            i = int(i)
            Persona.objects.get(id=i).delete()
            return True
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404
    
#mio
# <- ---------------------------------------------------------------------------------- ->

def get_name_empresa(i=None):
    if i is not None:
        try:
            i = int(i)
            p = Empresa.objects.get(id=i)
            return EmpresaSerializer(p).data
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404

def traer_empresa(request):
    p = Empresa.objects.all()
    return EmpresaSerializer(p, context={"request": request}, many=True).data

def guardar_empresa(**kwargs):
    if 'user' in kwargs and kwargs.get('user') != "" and type(kwargs.get('user')) == str:
        p = Empresa.objects.create(name = kwargs.get('user'))
        p.nombre_empresa = kwargs.get('nombre_empresa') if 'nombre_empresa' in kwargs else None
        p.save()
        return True
    else:
        return False
    
def borrar_empresa(i=None):
    if i is not None:
        try:
            i = int(i)
            Empresa.objects.get(id=i).delete()
            return True
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404
    
# <- ----------------------------------------------------------------------------------------------- ->

def get_name_GrupoTrabajo(i=None):
    if i is not None:
        try:
            i = int(i)
            p = GrupoTrabajo.objects.get(id=i)
            return GrupoTrabajoSerializer(p).data
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404

def traer_GrupoTrabajo(request):
    p = GrupoTrabajo.objects.all()
    return GrupoTrabajoSerializer(p, context={"request": request}, many=True).data

def guardar_GrupoTrabajo(**kwargs):
    if 'categoria' in kwargs and kwargs.get('categoria') != "" and type(kwargs.get('categoria')) == str:
        p = GrupoTrabajo.objects.create(name = kwargs.get('categoria'))
        p.empresa = kwargs.get('empresa') if 'empresa' in kwargs else None
        p.save()
        return True
    else:
        return False
    
def borrar_GrupoTrabajo(i=None):
    if i is not None:
        try:
            i = int(i)
            GrupoTrabajo.objects.get(id=i).delete()
            return True
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404

# <- ----------------------------------------------------------------------------------------------- ->

def get_name_Personal(i=None):
    if i is not None:
        try:
            i = int(i)
            p = Personal.objects.get(id=i)
            return PersonalSerializer(p).data
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404

def traer_Personal(request):
    p = Personal.objects.all()
    return PersonalSerializer(p, context={"request": request}, many=True).data

def guardar_Personal(**kwargs):
    if 'user' in kwargs and kwargs.get('user') != "" and type(kwargs.get('user')) == str:
        p = Personal.objects.create(name = kwargs.get('user'))
        p.nombre = kwargs.get('nombre') if 'nombre' in kwargs else None
        p.grupo_trabajo = kwargs.get('grupo_trabajo') if 'grupo_trabajo' in kwargs else None
        p.save()
        return True
    else:
        return False
    
def borrar_Personal(i=None):
    if i is not None:
        try:
            i = int(i)
            Producto.objects.get(id=i).delete()
            return True
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404

# <- ----------------------------------------------------------------------------------------------- ->

def get_name_producto(i=None):
    if i is not None:
        try:
            i = int(i)
            p = Producto.objects.get(id=i)
            return ProductoSerializer(p).data
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404

def traer_producto(request):
    p = Producto.objects.all()
    return ProductoSerializer(p, context={"request": request}, many=True).data

def guardar_producto(**kwargs):
    if 'nombre_producto' in kwargs and kwargs.get('nombre_producto') != "" and type(kwargs.get('nombre_producto')) == str:
        p = Producto.objects.create(name = kwargs.get('nombre_producto'))
        p.cantidad_producto = kwargs.get('cantidad_producto') if 'cantidad_producto' in kwargs else None
        p.precio_producto = kwargs.get('precio_producto') if 'precio_producto' in kwargs else None
        p.categoria_producto = kwargs.get('categoria_producto') if 'categoria_producto' in kwargs else None
        p.save()
        return True
    else:
        return False
    
def borrar_producto(i=None):
    if i is not None:
        try:
            i = int(i)
            Producto.objects.get(id=i).delete()
            return True
        except Exception as e:
            print(e)
            raise Http404
    else:
        raise Http404