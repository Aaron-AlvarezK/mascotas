from django.db import models
from django.contrib.auth.models import AbstractUser

class Mascotas(models.Model):
   nombre = models.CharField(max_length=100)
   raza = models.CharField(max_length=100)
   descripcion = models.TextField()
   foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)

   def __str__(self):
      return f'{self.nombre} ({self.raza})'

   class Meta:
      db_table = 'mascota'
      verbose_name = 'Mascota'
      verbose_name_plural = 'Mascotas'


class Cliente(models.Model):
   run_cliente = models.CharField('Run Cliente', max_length=10, unique=True)
   nombre_cliente = models.CharField('Nombre Cliente', max_length=100)
   apellido = models.CharField(max_length=100)
   correo = models.TextField()
   telefono = models.CharField(max_length=12)

   def __str__(self):
      return f'{self.nombre_cliente} {self.apellido} ({self.run_cliente})'


class Solicitud(models.Model):
   id = models.IntegerField(primary_key=True)
   run_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='solicitudes')
   nombre_mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE, related_name='solicitudes')
   detalle = models.TextField()
   fecha = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'Solicitud #{self.id} - {self.run_cliente}'


