from django.db import models

# Create your models here.

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    exportacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


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
    imagenCliente = models.URLField(max_length=600, null= True, blank= True)

    def __str__(self):
        nombreCompleto = self.nombre + ' ' + self.apellido
        return nombreCompleto

class Marca(models.Model):
    select_tipo = (
        ('Cigarrillos', 'Cigarrillos'),
        ('Puros', 'Puros'),
    )

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length= 20, choices= select_tipo)
    estanco = models.ForeignKey(Estanco, related_name='marcas', on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidor, related_name='marca', on_delete=models.CASCADE)
    imagenMarca = models.URLField(max_length=600, null= True, blank= True)

    def __str__(self):
        return self.nombre
    

class Cigarrillo(models.Model):
    select_tipo = (
        ('Industriales', 'Industriales'),
        ('De liar', 'De liar'),
    )
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length= 20, choices= select_tipo)
    precio = models.FloatField()
    marca = models.ForeignKey(Marca, related_name='cigarro', on_delete=models.CASCADE, default=False)
    imagenCig = models.URLField(max_length=600, null= True, blank= True)

    def __str__(self):
        return self.nombre

class Puro(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    precio = models.FloatField()
    marca = models.ForeignKey(Marca, related_name='puro', on_delete=models.CASCADE, default=False)
    imagenPuro = models.URLField(max_length=600, null= True, blank= True)

    def __str__(self):
        return self.nombre