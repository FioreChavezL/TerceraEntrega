from django import forms

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField(max_length = 60)
    apellido = forms.CharField(max_length = 60)
    correo = forms.EmailField()


class ProveedorFormulario(forms.Form):
    
    empresa = forms.CharField(max_length = 60)
    nombre_representante_legal = forms.CharField(max_length = 60)
    apellido_representante_legal = forms.CharField(max_length = 60)
    correo_empresa = forms.EmailField()

class TiendaFormulario(forms.Form):
    empresa = forms.CharField(max_length=60)
    tienda = forms.CharField(max_length=60)
    pais = forms.CharField(max_length = 60)
    provincia = forms.CharField(max_length = 60)
    distrito = forms.CharField(max_length = 60)
    direccion = forms.CharField(max_length = 60)