from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Distribuidor, Estanco, Cliente, Marca
# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaDistribuidores(request):
    distribuidor = Distribuidor.objects.order_by('nombre')
    contexto = {'lista_distribuidores': distribuidor}
    return render(request, 'listaDistribuidores.html', contexto)
        
def listaEstancos(request):
    estanco = Estanco.objects.order_by('nombre')
    contexto = {'lista_estancos': estanco}
    return render(request, 'listaEstancos.html', contexto)

def listaClientes(request):
    cliente = Cliente.objects.order_by('nombre')
    contexto = {'lista_clientes': cliente}
    return render(request, 'listaClientes.html', contexto)

def detalleDistribuidores(request, id_distribuidor):
    distribuidor = get_object_or_404(Distribuidor, pk=id_distribuidor)
    contexto = {'distribuidor': distribuidor}
    return render(request, 'detalleDistribuidores.html', contexto)

def detalleEstancos(request, id_estanco):
    estanco = get_object_or_404(Estanco, pk=id_estanco)
    contexto = {'estanco': estanco}
    return render(request, 'detalleEstancos.html', contexto)

def detalleClientes(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    contexto = {'cliente': cliente}
    return render(request, 'detalleClientes.html', contexto)
 
def detalleMarcas(request, id_marca):
    marca = get_object_or_404(Marca, pk=id_marca)
    contexto = {'marca': marca}
    return render(request, 'detalleMarcas.html', contexto)

def listaMarcas(request, id_marca):
    marca = marca.objects.order_by('nombre')
    contexto = {'lista_marcas': marca}
    return render(request, 'listaMarcas.html', contexto)