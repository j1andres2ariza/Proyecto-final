from django.shortcuts import render
from django.http import HttpResponse
from .models import Clientes, Empleados
# Create your views here.

def mclientes(request):
    cliente = Clientes.objects.all().values("nombre", "apellido", "direccion", "telefono", "email", "nombreEmpleado__nombre", "nombreEmpleado__apellido")
    responsevar = "<h2> Hola </h2>"
    for i in cliente:
        responsevar += f"Nombre: {i['nombre']} <br> Apellido: {i['apellido']} <br> Dirección: {i['direccion']} <br> Teléfono: {i['telefono']} <br> Email: {i['email']} <br> Nombre Empleado: {i['nombreEmpleado__nombre']} <br> Apellido Empleado: {i['nombreEmpleado__apellido']}"
    return HttpResponse(responsevar)