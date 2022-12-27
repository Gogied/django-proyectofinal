from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1"]

class agregarProductosForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'
        labels= {
            'user': 'Vendedor',
            'estado_id': 'Estado del Producto',
            'categoria_id': 'Categoria',
            'envio_id': 'Tiene envio?'
        }
        exclude = ['aprobado_id']

class CarruselForm(forms.ModelForm):
    class Meta:
        model = carrusel
        fields = '__all__'