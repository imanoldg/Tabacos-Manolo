from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'listaE'),

    path('listadoClientes/', views.listaClientes, name = 'listaClientes'), 
    path('DetalleClientes/', views.detalleClientes, name = 'detalleClientes'),

    path('listadoDistribuidores/', views.listaDistribuidores, name = 'listaDistribuidores'), 
    path('DetalleDistribuidores/', views.detalleDistribuidores, name = 'detalleDistribuidores'),

    path('listadoEstancos/', views.listaEstancos, name = 'listaEstancos'), 
    path('DetalleEstancos/', views.detalleEstancos, name = 'detalleEstancos'),
]