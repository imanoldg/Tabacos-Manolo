from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Distribuidor, Estanco, Cliente, Marca, Cigarrillo, Puro
from django.views.generic import ListView, DetailView
# Create your views here.
def index(request):
    return render(request, 'index.html')

class listaDistribuidoresView(ListView):
    model = Distribuidor
    template_name = 'listaDistribuidores.html'
    queryset = Distribuidor.objects.order_by('nombre')
        
class listaEstancosView(ListView):
    model = Estanco
    template_name = 'listaEstancos.html'
    queryset = Estanco.objects.order_by('nombre')

class listaClientesView(ListView):
    model = Cliente
    template_name = 'listaClientes.html'
    queryset = Cliente.objects.order_by('nombre')

class detalleDistribuidoresView(DetailView):
    model = Distribuidor
    template_name = 'detalleDistribuidores.html'

class detalleEstancosView(DetailView):
    model = Estanco
    template_name = 'detalleEstancos.html'

class detalleClientesView(DetailView):
    model = Cliente
    template_name = 'detalleClientes.html'
 
def detalleMarcas(request, id_marca):
    marca = get_object_or_404(Marca, pk=id_marca)
    estancos = marca.estanco.all()
    contexto = {'marca': marca, 'estancos': estancos}
    return render(request, 'detalleMarcas.html', contexto)

class listaMarcasView(ListView):
    model = Marca
    template_name = 'listaMarcas.html'
    queryset = Marca.objects.order_by('nombre')

def detalleCigarro(request, id_cigar):
    cigar = get_object_or_404(Cigarrillo, pk=id_cigar)
    contexto = {'cigar': cigar}
    return render(request, 'detalleCigarrillo.html', contexto)

class listaCigarrillosView(ListView):
    model = Cigarrillo
    template_name = 'listaCigarrillos.html'
    queryset = Cigarrillo.objects.order_by('nombre')

class detallePuroView(DetailView):
    model = Puro
    template_name = 'detallePuro.html'

class listaPurosView(ListView):
    model = Puro
    template_name = 'listaPuros.html'
    queryset = Puro.objects.order_by('nombre')