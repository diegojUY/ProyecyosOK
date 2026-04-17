from django import forms
from .models import Contacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'consulta']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Tu nombre',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Tu correo electrónico',
                'required': True
            }),
            'consulta': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Cuéntame tu consulta...',
                'rows': 6,
                'required': True
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo Electrónico',
            'consulta': 'Consulta',
        }
