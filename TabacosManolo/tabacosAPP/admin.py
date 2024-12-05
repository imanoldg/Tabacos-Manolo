from django.contrib import admin
from .models import Distribuidor, Estanco, Cliente, Marca, Cigarrillo, Puro

admin.site.site_header = 'Tabacos Manolo Admin'

# Register your models here.
admin.site.register(Distribuidor)
admin.site.register(Estanco)
admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Cigarrillo)
admin.site.register(Puro)
