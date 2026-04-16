from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length = 30)
    domicilio = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 60)
    estado = models.CharField(max_length = 50)
    pais = models.CharField(max_length = 50)
    sitioweb = models.URLField()

class Usuario(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 50)
    email = models.EmailField()