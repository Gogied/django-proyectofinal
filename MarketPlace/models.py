from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class estado_producto(models.Model):
    estado_id = models.AutoField(primary_key= True, verbose_name='estado_id')
    descripcion = models.CharField(max_length= 20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion

class categoria(models.Model):
    categoria_id = models.AutoField(primary_key= True, verbose_name='categoria_id')
    descripcion = models.CharField(max_length= 20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion
    
class envio(models.Model):
    envio_id = models.AutoField(primary_key= True, verbose_name='envio_id')
    descripcion = models.CharField(max_length= 20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion

class aprobado(models.Model):
    aprobado_id = models.AutoField(primary_key= True, verbose_name='aprobado_id')
    descripcion = models.CharField(max_length= 20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion

class producto(models.Model):
    id = models.AutoField(primary_key= True, verbose_name='id')
    titulo = models.CharField(max_length=30, verbose_name='titulo')
    descripcion = models.TextField(max_length= 255, verbose_name='descripcion')
    precio = models.IntegerField(verbose_name='precio')
    fecha_ingreso= models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="productos", null=True)
   

# Claves foraneas (Relaciona las tablas con la principal "Producto")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estado_id = models.ForeignKey(estado_producto, on_delete=models.SET(4))
    categoria_id = models.ForeignKey(categoria, on_delete=models.SET(4))
    envio_id = models.ForeignKey(envio, on_delete=models.SET(2))
    aprobado_id = models.ForeignKey(aprobado, on_delete=models.CASCADE, default=2)
    

    def __str__(self):
        return self.titulo

class carrusel(models.Model):
    id_carrusel = models.AutoField(primary_key= True, verbose_name='id_carrusel')
    imagen_carrusel = models.ImageField(upload_to="carrusel", null=True)
    imagen_carrusel2 = models.ImageField(upload_to="carrusel", null=True)
    imagen_carrusel3 = models.ImageField(upload_to="carrusel", null=True)

    def __str__(self):
        return str(self.id_carrusel)

