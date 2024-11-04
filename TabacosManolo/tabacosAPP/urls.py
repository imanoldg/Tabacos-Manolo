from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'listaE'),

    path('listadoClientesConPlantillas/', views.listaClientes, name = 'listaClientesPlantillas'), 
    path('DetalleClientesConPlantillas/', views.detalleClientes, name = 'detalleClientesPlantillas'),

    path('listadoDistribuidoresConPlantillas/', views.listaDistribuidores, name = 'listaDistribuidoresPlantillas'), 
    path('DetalleDistribuidoresConPlantillas/', views.detalleDistribuidores, name = 'detalleDistribuidoresPlantillas'),

    path('listadoEstancosConPlantillas/', views.listaEstancos, name = 'listaEstancosPlantillas'), 
    path('DetalleEstancosConPlantillas/', views.detalleEstancos, name = 'detalleEstancosPlantillas'),

]