from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=50, primary_key=True, unique=True, blank=False)
    tipo_empresa = models.BooleanField(default=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.id_cliente} - {self.tipo()}"

    def tipo(self):
        return "Empresa" if self.tipo_empresa else "Persona"


#modelo de entrada
class Entrada(models.Model):
    id_entrada = models.CharField(max_length=50, primary_key=True, unique=True, blank=False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
