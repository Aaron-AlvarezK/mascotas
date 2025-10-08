from django.shortcuts import render
from mascotas.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SolicitudForm
from .forms import ClienteForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def mascotaData(request):
    mascota = Mascotas.objects.all()
    data = {'mascotas': mascota}
    return render(request,'galeria.html',data)



def home(request):
    return render(request, 'galeria.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado con éxito.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña no válidos.')
    return render(request, 'login.html')


def es_superusuario(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(es_superusuario)
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado correctamente.')
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})

@user_passes_test(es_superusuario)
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre_cliente')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

@user_passes_test(es_superusuario)
def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('-fecha')
    return render(request, 'solicitudes/solicitudes.html', {'solicitudes': solicitudes})

@user_passes_test(es_superusuario)
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud creada correctamente.')
            return redirect('solicitudes/solicitudes.html')  
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/crear_solicitud.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')





