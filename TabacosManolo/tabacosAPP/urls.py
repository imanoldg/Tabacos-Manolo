from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    path('listadoClientes/', views.listaClientes, name='listaClientes'), 
    path('DetalleClientes/<int:id_cliente>/', views.detalleClientes, name='detalleClientes'),  

    path('listadoDistribuidores/', views.listaDistribuidores, name='listaDistribuidores'), 
    path('DetalleDistribuidores/<int:id_distribuidor>/', views.detalleDistribuidores, name='detalleDistribuidores'),  

    path('listadoEstancos/', views.listaEstancos, name='listaEstancos'), 
    path('DetalleEstancos/<int:id_estanco>/', views.detalleEstancos, name='detalleEstancos'),

    path('listadoMarcas/', views.listaMarcas, name= 'listaMarcas'),
    path('DetalleMarcas/ <int: id_marca>/', views.detalleMarcas, name='detalleMarcas'),  
]