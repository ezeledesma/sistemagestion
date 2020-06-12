from django.db import models
from datetime import datetime, date


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


class Articulo (models.Model):

    codigo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=40)
    marca=models.CharField(max_length=20)
    medida=models.CharField(max_length=20)
    cantidad=models.IntegerField()
    lote=models.CharField(max_length=20)
    vencimiento=models.DateField()
    deposito=models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion


class Historial (models.Model):
    
    fecha=models.DateField(blank=True)
    # fecha=models.CharField(max_length=20)
    operacion=models.CharField(max_length=20)
    codigo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=40)
    marca=models.CharField(max_length=20)
    medida=models.CharField(max_length=20)
    cantidad=models.IntegerField()
    lote=models.CharField(max_length=20)
    vencimiento=models.DateField()
    deposito=models.CharField(max_length=30)
    remito=models.CharField(max_length=20)
    usuario=models.CharField(max_length=20)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

