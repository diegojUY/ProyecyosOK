from django.urls import path
from . import views

app_name = 'muestras'

urlpatterns = [
    path('', views.galeria_diseños, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
]
