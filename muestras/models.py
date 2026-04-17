from django.db import models

class DesignoWeb(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    url = models.URLField()
    imagen_preview = models.ImageField(upload_to='previews/', blank=True, null=True)
    tecnologias = models.CharField(max_length=300, help_text="Ej: HTML, CSS, JavaScript")
    fecha_creacion = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    consulta = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"Contacto de {self.nombre} - {self.fecha_creacion.strftime('%d/%m/%Y')}"


class ProyectoWeb(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    url = models.URLField()
    imagen = models.ImageField(upload_to='proyectos/')
    icono = models.CharField(
        max_length=50, 
        default='🌐',
        help_text="Emoji o ícono para la tarjeta"
    )
    tecnologias = models.CharField(
        max_length=300, 
        help_text="Ej: React, Node.js, MongoDB"
    )
    orden = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['orden', '-fecha_creacion']
    
    def __str__(self):
        return self.titulo
