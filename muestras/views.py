from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import DesignoWeb, Contacto, ProyectoWeb
from .forms import FormularioContacto

def galeria_diseños(request):
    diseños = DesignoWeb.objects.all()
    proyectos = ProyectoWeb.objects.all()
    contexto = {
        'diseños': diseños,
        'proyectos': proyectos,
    }
    return render(request, 'muestras/galeria.html', contexto)


def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            contacto_obj = form.save()
            
            # Enviar email al administrador
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            consulta = form.cleaned_data['consulta']
            
            asunto = f'Nuevo mensaje de contacto de {nombre}'
            mensaje = f"""
            Tienes un nuevo mensaje de contacto:
            
            Nombre: {nombre}
            Correo: {correo}
            
            Mensaje:
            {consulta}
            """
            
            try:
                send_mail(
                    asunto,
                    mensaje,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, '¡Gracias por tu consulta! Te responderé pronto.')
            except Exception as e:
                print(f"Error al enviar email: {e}")
                messages.success(request, '¡Gracias por tu consulta! Te responderé pronto.')
            
            return redirect('muestras:contacto')
    else:
        form = FormularioContacto()
    
    contexto = {
        'form': form,
        'correo': settings.ADMIN_EMAIL,
    }
    return render(request, 'muestras/contacto.html', contexto)
