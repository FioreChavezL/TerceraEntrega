from django.db import models

# Create your models here.
class clientes1(models.Model):
    
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 60)
    correo = models.EmailField()
    
class proveedores1(models.Model):

    empresa = models.CharField(max_length = 60)
    nombreRL = models.CharField(max_length = 60)
    apellidoRL = models.CharField(max_length = 60)
    correo_empresa = models.EmailField()

class tiendas1(models.Model):
    
    empresa = models.CharField(max_length=60)
    tienda = models.CharField(max_length=60)
    pais = models.CharField(max_length = 60)
    provincia = models.CharField(max_length = 60)
    distrito = models.CharField(max_length = 60)
    direccion = models.CharField(max_length = 60)



