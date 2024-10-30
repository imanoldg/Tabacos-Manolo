from django.contrib import admin
from .models import Distribuidor, Estanco, Cliente

# Register your models here.
admin.site.register(Distribuidor)
admin.site.register(Estanco)
admin.site.register(Cliente)