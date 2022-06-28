from django import forms

class NuevoSocio(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre")
    apellido = forms.CharField(max_length=30,label="Apellido")
    edad = forms.IntegerField(min_value=1,label="Edad")
    deportes = forms.CharField(max_length=30,label="Deportes")
    email = forms.EmailField(label="Email")

class NuevoProfesor(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre")   #cambiar
    apellido = forms.CharField(max_length=30,label="Apellido")
    deporte = forms.CharField(max_length=30,label="Deporte")
    email = forms.EmailField(label="Email")

class NuevoDeporte(forms.Form):
    deporte = forms.CharField(max_length=30,label="Deporte")
    profesor = forms.CharField(max_length=70,label="Profesor")
    horario = forms.CharField(label="Horario")
    
class NuevoAdministrador(forms.Form):
    puesto = forms.CharField(max_length=100,label="Puesto")
    nombre = forms.CharField(max_length=30,label="Nombre")
    apellido = forms.CharField(max_length=30,label="Apellido")
    email = forms.EmailField(label="Email")

