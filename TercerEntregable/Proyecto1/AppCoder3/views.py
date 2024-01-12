from django.shortcuts import render
from django.http import HttpResponse
from AppCoder3.models import *
from AppCoder3.forms import *

def inicio(request):
    
    return render(request,"AppCoder3/inicio.html")

def clientes(request):

    return render(request,"AppCoder3/cliente.html")

def proveedores(request):

    return render(request,"AppCoder3/proveedor.html")

def tiendas(request):

    return render(request,"AppCoder3/tienda.html")

def clienteformulario(request):
    if request.method == "POST":
        
        formulario1 = ClienteFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cliente1 = clientes1(nombre=info["nombre"], apellido=info["apellido"],correo=info["correo"])
            cliente1.save()
        
            return render(request, "AppCoder3/inicio.html")
        
    else:
        formulario1 = ClienteFormulario()

    
    return render(request, "AppCoder3/cliente.html",{"form1":formulario1})


def proveedorformulario(request):
    if request.method == "POST":
        
        formulario1 = ProveedorFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cliente1 = proveedores1(empresa=info["empresa"], nombreRL=info["nombreRL"],apellidoRL=info["apellidoRL"], correo_empresa=info["correo_empresa"])
            cliente1.save()
        
            return render(request, "AppCoder3/inicio.html")
        
    else:
        formulario1 = ProveedorFormulario()

    
    return render(request, "AppCoder3/proveedor.html",{"form2":formulario1})

def tiendaformulario(request):
    if request.method == "POST":
        
        formulario1 = TiendaFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cliente1 = tiendas1(empresa=info["empresa"], tienda=info["tienda"],pais=info["pais"], provincia=info["provincia"], distrito=info["distrito"], direccion=info["direccion"])
            cliente1.save()
        
            return render(request, "AppCoder3/inicio.html")
        
    else:
        formulario1 = TiendaFormulario()

    
    return render(request, "AppCoder3/tienda.html",{"form3":formulario1})

def busquedatienda(request):
    return render(request, "AppCoder3/inicio.html")

def resultadotienda(request):
    if request.GET['empresa']:

        empresa = request.GET["empresa"]
        tienda = tiendas1.objects.filter(empresa__icontains=empresa)

        return render(request,"AppCoder3/inicio.html",{"tienda":tienda, "empresa":empresa})
    else:
        respuesta = "No ingresaste ningún dato"

    return HttpResponse(respuesta)
  