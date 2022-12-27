from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    prod = producto.objects.filter(aprobado_id=1)
    carrus = carrusel.objects.all()
    data = {
        'productos': prod,
        'carrusel': carrus
    }
    return render(request, 'home.html', data)

def registro(request):
    data = {
        'form':CustomCreationForm
    }
    if request.method == 'POST':
        form = CustomCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = form
    return render(request, 'registration/registro.html', data)

def misProductos(request):
    current = request.user
    prod = producto.objects.filter(user = current.id, aprobado_id=1)
    data = {
        'productos': prod
    }
    return render(request, 'cliente/mis_productos.html', data)

def agregarProducto(request):
    current = request.user
    initial_data={
        'user':current.id
    }
    data = {
        'form':agregarProductosForm(initial=initial_data)
    }
    if request.method == 'POST':
        formulario = agregarProductosForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'cliente/mis_productos.html', data)
        else:
            return render(request, 'cliente/agregar_productos.html', data)
    return render(request, 'cliente/agregar_productos.html', data)

def modificarProducto(request, id):
    product = get_object_or_404(producto, id=id)

    data={
        'form':agregarProductosForm(instance=product)
    }
    if request.method == 'POST':
        formulario = agregarProductosForm(request.POST, files=request.FILES, instance=product)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="misPrds")
        else:
            print(formulario.is_valid())
            return redirect(to="misPrds")
    return render(request, 'cliente/modificar_productos.html', data)

def ELIMINACIONLOGICA(request, id):
    producto.objects.filter(id=id).update(aprobado_id=2)
    return redirect(to="misPrds")