from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PersonaForm, CategoriaForm, ProductoForm, ContactoForm, OrdenForm
from .models import Orden_compra
from django.views.generic.edit import CreateView

def index(request, template_name="main/index.html"):
    return render(request, template_name)

def cargar_cliente(request, template_name="main/nuevo_cliente.html"):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("nuevocliente") # Esto es para que al cargar al cliente, retorne a la página donde tengo el listado
    else:
        form = PersonaForm()
    datos = {"form": form}
    return render(request, template_name, datos)

def nueva_orden(request, template_name="main/nueva_orden.html"):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("ordenes") # Esto es para que al cargar al cliente, retorne a la página donde tengo el listado
    else:
        form = OrdenForm()
    datos = {"form": form}
    return render(request, template_name, datos)

def orden(request, template_name="main/ordenes.html"):
    ordenes_list = Orden_compra.objects.all()
    datos = {"ordenes": ordenes_list}
    return render(request, template_name, datos)

def contacto(request, template_name="main/contacto.html"):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("index") # Esto es para que al cargar al cliente, retorne a la página donde tengo el listado
    else:
        form = ContactoForm()
    datos = {"form": form}
    return render(request, template_name, datos)