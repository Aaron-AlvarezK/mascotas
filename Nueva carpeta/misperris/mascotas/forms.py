from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario'
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['run_cliente', 'nombre_mascota', 'detalle']  
        labels = {
            'run_cliente': 'Cliente',
            'nombre_mascota': 'Mascota',
            'detalle': 'Detalle de la solicitud',
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['run_cliente', 'nombre_cliente', 'apellido', 'correo', 'telefono']