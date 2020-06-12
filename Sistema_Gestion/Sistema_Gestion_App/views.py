from django.shortcuts import render, HttpResponse
from Sistema_Gestion_App.models import Articulos, Historial
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Sum

from django.utils import timezone
from datetime import datetime


# Globals
articulos=Articulos()
historiales=Historial()
user=User()
ordername=True

# Views
@login_required
def inicio(request):
    return render(request, "inicio.html")

@login_required
def menu(request):
    return render(request, "menu.html")

#### Inventario ####
@login_required
def inventario (request):
    global articulos
    articulos=Articulos.objects.filter(nombre__icontains="")
    return render(request, "inventario/inventario.html",{"articulos":articulos})

def codigo(request):
    print("prueba superada")
    return inventario(request)

def nombre(request):
    global ordername
    if ordername:
        articulos=Articulos.objects.filter(nombre__icontains="").order_by("nombre")
        ordername=False
    else:
        articulos=Articulos.objects.filter(nombre__icontains="").order_by("-nombre")
        ordername=True
    return render(request, "inventario/inventario.html",{"articulos":articulos})

@login_required
def cargar (request):
    global historiales
    historiales=Historial()
    historiales=Historial.objects.filter(descripcion__icontains="")
    if request.method=="POST":
        fecha = datetime.now
        nuevo=Historial()
        if 'Buscar' in request.POST:

            print ("Hay que buscar")
            nuevo.codigo=request.POST['Codigo']
            nuevo.descripcion=request.POST['Descripcion']
            nuevo.marca=request.POST['Marca']
            nuevo.medida=request.POST['Medida']
            nuevo.lote=request.POST['Lote']
            nuevo.deposito=request.POST['Deposito']
            historiales=Historial.objects.filter(codigo__icontains=nuevo.codigo).filter(descripcion__icontains=nuevo.descripcion).filter(marca__icontains=nuevo.marca).filter(medida__icontains=nuevo.medida).filter(lote__icontains=nuevo.lote).filter(deposito__icontains=nuevo.deposito)

        elif 'Retirar' in request.POST:
            print("Hay que retirar")

        elif 'Ingresar' in request.POST:

            if request.POST['Fecha']: 
                nuevo.fecha=request.POST['Fecha']
            else:
                nuevo.fecha=fecha().strftime("%Y-%m-%d")
            nuevo.operacion="INGRESO"
            nuevo.codigo=request.POST['Codigo']
            nuevo.descripcion=request.POST['Descripcion']
            nuevo.marca=request.POST['Marca']
            nuevo.medida=request.POST['Medida']
            nuevo.cantidad=request.POST['Cantidad']
            nuevo.lote=request.POST['Lote']
            nuevo.vencimiento=request.POST['Vencimiento']
            nuevo.deposito=request.POST['Deposito']
            nuevo.usuario=request.user.username
            nuevo.save()

        else:
            print("Error en la view cargar :(")
    return render(request, "inventario/cargar.html",{"historiales":historiales})

@login_required
def editar(request):
    return render(request, "inventario/editar.html")

@login_required
def reservar(request):
    return render(request, "inventario/reservar.html")

@login_required
def historial (request):
    global historiales
    historiales=Historial.objects.filter(descripcion__icontains="")
    return render(request, "inventario/historial.html",{"historiales":historiales})

#### Fin inventario ####

@login_required
def pedidos (request):
    return render(request, "pedidos.html")

@login_required
def clientes (request):
    return render(request, "clientes.html")

@login_required
def proveedores (request):
    return render(request, "proveedores.html")

@login_required
def cotizacion (request):
    return render(request, "cotizacion.html")

def salir (request):
    return inicio(request)
