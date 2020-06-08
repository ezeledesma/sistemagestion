from django.shortcuts import render, HttpResponse
from Sistema_Gestion_App.models import Articulos
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Globals
articulos=Articulos()
user=User()

# Views
@login_required
def inicio(request):
    return render(request, "inicio.html")

@login_required
def menu(request):
    return render(request, "menu.html")

@login_required
def inventario (request):
    global articulos
    articulos=Articulos.objects.filter(nombre__icontains="")
    return render(request, "inventario.html",{"articulos":articulos})

@login_required
def cargar (request):
    if request.method=="POST":
        nuevo=Articulos()
        nuevo.seccion=request.POST['Seccion']
        nuevo.nombre=request.POST['Nombre']
        nuevo.marca=request.POST['Marca']
        nuevo.unidad=request.POST['Unidad']
        nuevo.cantidad=request.POST['Cantidad']
        nuevo.precio=request.POST['Precio']
        nuevo.codigo=request.POST['Codigo']
        nuevo.lote=request.POST['Lote']
        nuevo.save()
    return render(request, "cargar.html")

@login_required
def pedidos (request):
    return HttpResponse("Pedidos")

@login_required
def clientes (request):
    return HttpResponse("Clientes")

@login_required
def proveedores (request):
    return HttpResponse("Proveedores")

@login_required
def cotizacion (request):
    return HttpResponse("Cotizacion")

def salir (request):
    return inicio(request)
