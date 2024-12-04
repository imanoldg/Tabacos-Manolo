from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    path('listadoClientes/', views.listaClientesView.as_view(), name='listaClientes'), 
    path('DetalleClientes/<int:pk>/', views.detalleClientesView.as_view(), name='detalleClientes'),  

    path('listadoDistribuidores/', views.listaDistribuidoresView.as_view(), name='listaDistribuidores'), 
    path('DetalleDistribuidores/<int:pk>/', views.detalleDistribuidoresView.as_view(), name='detalleDistribuidores'),  

    path('listadoEstancos/', views.listaEstancosView.as_view(), name='listaEstancos'), 
    path('DetalleEstancos/<int:pk>/', views.detalleEstancosView.as_view(), name='detalleEstancos'),

    path('listadoMarcas/', views.listaMarcasView.as_view(), name= 'listaMarcas'),
    path('DetalleMarcas/ <int:id_marca>/', views.detalleMarcas, name='detalleMarcas'),

    path('listadoCigarros/', views.listaCigarrillosView.as_view(), name= 'listaCigarros'),
    path('DetalleCigarros/ <int:id_cigar>/', views.detalleCigarro, name='detalleCigarro'),  

    path('listadoPuros/', views.listaPurosView.as_view(), name= 'listaPuros'),
    path('DetallePuros/ <int:pk>/', views.detallePuroView.as_view(), name='detallePuro'),  
    
]