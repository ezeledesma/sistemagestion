from django.urls import path, include
from Sistema_Gestion_App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('menu', views.menu, name="Menu"),
    path('inventario', views.inventario, name="Inventario"),
    path('cargar', views.cargar, name="Cargar"),
    path('pedidos', views.pedidos, name="Pedidos"),
    path('clientes', views.clientes, name="Clientes"),
    path('proveedores', views.proveedores, name="Proveedores"),
    path('cotizacion', views.cotizacion, name="Cotizacion"),
    path('salir', views.salir, name="Salir"),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]