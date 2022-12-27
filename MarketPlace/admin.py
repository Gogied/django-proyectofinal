from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class PubliarAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

admin.site.register(producto)

admin.site.register(estado_producto)

admin.site.register(categoria)

admin.site.register(envio)

admin.site.register(carrusel)

admin.site.register(aprobado)
