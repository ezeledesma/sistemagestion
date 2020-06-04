from django.urls import path, include
from Sistema_Gestion_App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('stock', views.stock, name="Stock"),
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