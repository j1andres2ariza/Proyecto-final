from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    nombreEmpleado = models.ForeignKey('Empleados', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Cliente: {'{} {}'.format(self.nombre, self.apellido)}-Empleado: {'{} {}' .format(self.nombreEmpleado.nombre, self.nombreEmpleado.apellido)}"
    
class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    salario = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)