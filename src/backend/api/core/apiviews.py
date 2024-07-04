from tokenize import Token 
from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from apps.core import utils

class Persona(APIView):
    def get(self,request, persona_id):
        response = utils.get_name(persona_id)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)
    
    def post(self, request, format='json'):
        saved = utils.guardar_persona(request.data)
        status_code = status.HTTP_200_OK if saved else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)
    
    def update():
        pass
    
    def delete(self, resquest, persona_id):
        deleted = utils.borrar_persona(persona_id)
        status_code = status.HTTP_200_OK if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)
    
class ListPersona(APIView):
    def get(self,request):
        response = utils.traer_personas(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)

#mio 
# <- ---------------------------------------------------------------------------------------------- ->

class Empresa(APIView):
    def post(self,request, format='json'):
        saved = utils.guardar_empresa(request.data)
        status_code = status.HTTP_200_OK if saved else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)
    
    def get(self,request, empresa_id):
        response = utils.get_name_empresa(empresa_id)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)
    
    def update():
        pass

    def delete(self, resquest, empresa_id):
        deleted = utils.borrar_empresa(empresa_id)
        status_code = status.HTTP_200_OK if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class ListEmpresa(APIView):
    def get(self,request):
        response = utils.traer_empresa(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)

# <- ---------------------------------------------------------------------------------- ->

class GrupoTrabajo(APIView):
    def post(self,request, format='json'):
        saved = utils.guardar_GrupoTrabajo(request.data)
        status_code = status.HTTP_200_OK if saved else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)
    
    def get(self,request, grupoTrabajo_id):
        response = utils.get_name_GrupoTrabajo(grupoTrabajo_id)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)
    
    def update():
        pass

    def delete(self, resquest, grupoTrabajo_id):
        deleted = utils.borrar_GrupoTrabajo(grupoTrabajo_id)
        status_code = status.HTTP_200_OK if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class ListGrupoTrabajo(APIView):
    def get(self,request):
        response = utils.traer_GrupoTrabajo(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)

# <- --------------------------------------------------------------------------------- ->

class Personal(APIView):
    def post(self,request, format='json'):
        saved = utils.guardar_Personal(request.data)
        status_code = status.HTTP_200_OK if saved else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)
    
    def get(self,request, personal_id):
        response = utils.get_name_Personal(personal_id)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)
    
    def update():
        pass

    def delete(self, resquest, personal_id):
        deleted = utils.borrar_Personal(personal_id)
        status_code = status.HTTP_200_OK if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class ListPersonal(APIView):
    def get(self,request):
        response = utils.traer_Personal(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)

# <- --------------------------------------------------------------------------------- ->

class Producto(APIView):
    def post(self,request, format='json'):
        saved = utils.guardar_producto(request.data)
        status_code = status.HTTP_200_OK if saved else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)
    
    def get(self,request, producto_id):
        response = utils.get_name_producto(producto_id)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)
    
    def update():
        pass

    def delete(self, resquest, producto_id):
        deleted = utils.borrar_producto(producto_id)
        status_code = status.HTTP_200_OK if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class ListProducto(APIView):
    def get(self,request):
        response = utils.traer_producto(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status_code)