from django.db import models


class Articulos (models.Model):
    
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20, default='')
    cantidad=models.IntegerField(default=0)
    precio=models.IntegerField(default=0)
    marca=models.CharField(max_length=20, default='')
    unidad=models.CharField(max_length=20, default='')
    codigo=models.CharField(max_length=20, default='')
    lote=models.CharField(max_length=20, default='')

    def __str__(self):
        return self.nombre

