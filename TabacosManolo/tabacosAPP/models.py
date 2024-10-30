from django.db import models

# Create your models here.

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    exportacion = models.CharField(max_length=100)

    


class Estanco(models.Model):
    nombre = models.CharField(max_length=100)
    localizacion = models.CharField(max_length=150)
    distribuidor = models.ForeignKey(Distribuidor, related_name='estanco', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    estanco = models.ForeignKey(Estanco, related_name='clientes', on_delete=models.CASCADE)

    def __str__(self):
        nombreCompleto = self.nombre + ' ' + self.apellido
        return nombreCompleto

    