from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('registro/', registro, name='registro'),
    path('agregar_productos/', agregarProducto, name='agregarPrd'),
    path('mis_productos/', misProductos, name='misPrds'),
    path('modificar_productos/<id>/', modificarProducto, name='modificarPrd'),
    path('eliminacionLogica/<id>/', ELIMINACIONLOGICA, name='eliminacionLOGICA!')
]