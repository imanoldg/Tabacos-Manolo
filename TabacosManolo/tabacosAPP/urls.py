from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    path('listadoClientes/', views.listaClientes, name='listaClientes'), 
    path('DetalleClientes/<int:id_cliente>/', views.detalleClientes, name='detalleClientes'),  

    path('listadoDistribuidores/', views.listaDistribuidores, name='listaDistribuidores'), 
    path('DetalleDistribuidores/<int:id_distribuidor>/', views.detalleDistribuidores, name='detalleDistribuidores'),  

    path('listadoEstancos/', views.listaEstancosView.as_view(), name='listaEstancos'), 
    path('DetalleEstancos/<int:pk>/', views.detalleEstancosView.as_view(), name='detalleEstancos'),

    path('listadoMarcas/', views.listaMarcas, name= 'listaMarcas'),
    path('DetalleMarcas/ <int:id_marca>/', views.detalleMarcas, name='detalleMarcas'),

    path('listadoCigarros/', views.listaCigarrillos, name= 'listaCigarros'),
    path('DetalleCigarros/ <int:id_cigar>/', views.detalleCigarro, name='detalleCigarro'),  

    path('listadoPuros/', views.listaPuros, name= 'listaPuros'),
    path('DetallePuros/ <int:id_puro>/', views.detallePuro, name='detallePuro'),  
    
]