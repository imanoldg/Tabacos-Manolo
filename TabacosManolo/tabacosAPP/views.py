from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Distribuidor, Estanco, Cliente
# Create your views here.
def index(request):
    return HttpResponse("Bienvenido a la aplicacion de TabacosManolo")

def listaDistribuidores(request):
            distribuidores = Distribuidor.objects.order_by('nombre')
            nombres_distribuidores = ', '.join([distribuidor.nombre for distribuidor in distribuidores])
            return HttpResponse(nombres_distribuidores)
        
def listaEstancos(request):
            estancos = Estanco.objects.order_by('nombre')
            nombres_estancos = ', '.join([estanco.nombre for estanco in estancos])
            return HttpResponse(nombres_estancos)

def listaClientes(request):
            clientes = Cliente.objects.order_by('nombre')
            nombres_clientes = ', '.join([cliente.nombre for cliente in clientes])
            return HttpResponse(nombres_clientes)

def detalleDistribuidores(request, id_distribuidor):
            try:
                distribuidor = Distribuidor.objects.get(pk=id_distribuidor)

                cadenaDeTexto = f"Nombre: {distribuidor.nombre}\n - Pais: {distribuidor.pais}\n - Exportacion: {distribuidor.exportacion}\n"

                if distribuidor.estanco.exists():
                    cadenaDeTexto += f"Estancos:{distribuidor.estanco}\n"
                else:
                    cadenaDeTexto += "No hay estancos asociados a este distribuidor"

                return HttpResponse(cadenaDeTexto)
            except Distribuidor.DoesNotExist:
                return HttpResponseNotFound("Distribuidor no encontrado")
            
def detalleEstancos(request, id_estanco):
            try:
                estanco = Estanco.objects.get(pk=id_estanco)

                cadenaDeTexto = f"Nombre: {estanco.nombre}\n - Localizacion:{estanco.localizacion}\n"

                if estanco.clientes.exists():
                    cadenaDeTexto += f"Clientes:{estanco.clientes}\n"
                else:
                    cadenaDeTexto += "No hay clientes asociados a este estanco"

                return HttpResponse(cadenaDeTexto)
            except Estanco.DoesNotExist:
                return HttpResponseNotFound("Estanco no encontrado")

def detalleClientes(request, id_cliente):
            try:
                cliente = Cliente.objects.get(pk=id_cliente)

                cadenaDeTexto = f"DNI: {cliente.dni}\n - Nombre:{cliente.nombre}\n - Apellido: {cliente.apellido}\n - Edad: {cliente.edad}"

                if cliente.estanco.exists():
                    cadenaDeTexto += f"Estanco:{cliente.estanco}\n"
                else:
                    cadenaDeTexto += "No hay un estanco asociado a este cliente"

                return HttpResponse(cadenaDeTexto)
            except Cliente.DoesNotExist:
                return HttpResponseNotFound("Cliente no encontrado")
