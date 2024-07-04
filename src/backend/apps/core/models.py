from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    f_nacimiento = models.DateField(blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.FileField(upload_to='avatars/', max_length=100, blank=True, default='avatars/default.jpg')

#mio 
# <- ------------------------------------------------------------------------------------------ ->

class Empresa(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False, default="")
    password = models.CharField(max_length=50, blank=False, null=False, default="")
    nombre_empresa = models.CharField(max_length=100, blank=False)

class GrupoTrabajo(models.Model):
    class CategoriaChoices(models.TextChoices):
        ELECTRONICA = 'EL', 'Electrónica'
        ROPA = 'RO', 'Ropa'
        ALIMENTOS = 'AL', 'Alimentos'
        LIBROS = 'LI', 'Libros'
    
    categoria = models.CharField(
        max_length=2,
        choices=CategoriaChoices.choices,
        default=CategoriaChoices.ELECTRONICA
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='grupos_trabajo')

class Personal(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False, default="")
    password = models.CharField(max_length=50, blank=False, null=False, default="")
    nombre = models.CharField(max_length=50)
    grupo_trabajo = models.ManyToManyField(GrupoTrabajo, related_name='personal')

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    cantidad_producto = models.IntegerField(default=0, blank=True, null=True)
    precio_producto = models.IntegerField(default=0, blank=True, null=True)
    grupo_trabajo = models.ForeignKey(GrupoTrabajo, on_delete=models.CASCADE, related_name='productos', default=1)
