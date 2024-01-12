from django.urls import path
from AppCoder3.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cliente/', clientes,name="Clientes"),
    path('proveedor/', proveedores, name="Proveedores"),
    path('tienda/', tiendas, name="Tiendas"),
    path('clienteformulario/', clienteformulario,name="ClienteFormulario"),
    path('proveedorformulario/', proveedorformulario,name="ProveedorFormulario"),
    path('tiendaformulario/', tiendaformulario,name="TiendaFormulario"),
    path('buscartienda/', busquedatienda,name="BuscarTiendas"),
    path('resultadostienda/', resultadotienda,name="ResultadosTiendas"),
]