from django.contrib import admin
from django.urls import path
from mascotas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mascotaData, name='home'),
    path('galeria/', views.mascotaData, name='galeria'),

    
    path('solicitudes/', views.listar_solicitudes, name='solicitudes'),
    path('solicitudes/nueva/', views.crear_solicitud, name='crear_solicitud'),

    
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.crear_cliente, name='crear_cliente'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
]