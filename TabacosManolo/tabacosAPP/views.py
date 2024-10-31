from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Distribuidor, Estanco, Cliente
# Create your views here.
def index(request):
    return HttpResponse('primera vista')


def listaDis(request):
            empresas = Empresa.objects.order_by('nombre')
            nombres_empresas = ', '.join([empresa.nombre for empresa in empresas])
            return HttpResponse(nombres_empresas)

def detalleClientes(request, id_cliente):
            try:
                cliente = Cliente.objects.get(pk=id_cliente)

                # Crear la cadena de texto con los detalles de la empresa
                cadenaDeTexto = f"DNI: {cliente.dni}\n - Nombre:{cliente.nombre}\n - Apellido: {cliente.apellido}\n - Edad: {cliente.edad}"

                # Listar los trabajadores
                if cliente.estanco.exists():
                    cadenaDeTexto += f"Estanco:{cliente.estanco}\n"
                else:
                    cadenaDeTexto += "No hay un estanco asociado a este cliente"

                return HttpResponse(cadenaDeTexto)
            except Cliente.DoesNotExist:
                return HttpResponseNotFound("Cliente no encontrado")
