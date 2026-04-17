from django.contrib import admin
from .models import DesignoWeb, Contacto, ProyectoWeb

@admin.register(DesignoWeb)
class DesignoWebAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'descripcion', 'url')
        }),
        ('Medios', {
            'fields': ('imagen_preview',)
        }),
        ('Detalles Técnicos', {
            'fields': ('tecnologias', 'fecha_creacion')
        }),
    )


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'fecha_creacion', 'respondido')
    list_filter = ('fecha_creacion', 'respondido')
    search_fields = ('nombre', 'correo', 'consulta')
    readonly_fields = ('fecha_creacion', 'nombre', 'correo', 'consulta')
    fieldsets = (
        ('Información del Contacto', {
            'fields': ('nombre', 'correo', 'fecha_creacion')
        }),
        ('Mensaje', {
            'fields': ('consulta',)
        }),
        ('Estado', {
            'fields': ('respondido',)
        }),
    )


@admin.register(ProyectoWeb)
class ProyectoWebAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'orden', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    list_editable = ('orden',)
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Información General', {
            'fields': ('titulo', 'descripcion', 'url')
        }),
        ('Medios y Presentación', {
            'fields': ('imagen', 'icono')
        }),
        ('Detalles Técnicos', {
            'fields': ('tecnologias', 'orden', 'fecha_creacion')
        }),
    )
