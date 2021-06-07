from django.forms import ModelForm, DateInput
from django import forms
from .models import Persona, Categoria, Producto, Contacto, Orden_compra

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'email': forms.TextInput(),
            'activo': forms.CheckboxInput(),
            'fecha_carga': forms.HiddenInput(),
            'fecha_actualizacion': forms.HiddenInput(),
        }

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(),
            'descripcion': forms.TextInput(),
        }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'number', 'size': 3}),
            'nombre': forms.TextInput(),
            'categoria': forms.Select(),
            'precio': forms.TextInput(),
            'disponible': forms.CheckboxInput(),
            'fecha_carga': forms.HiddenInput(),
            'fecha_actualizacion': forms.HiddenInput(),
        }

class OrdenForm(ModelForm):
    class Meta:
        model = Orden_compra
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(),
            'producto': forms.SelectMultiple(),
        }

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'email': forms.TextInput(),
            'comentario': forms.Textarea(),
            'novedades': forms.CheckboxInput(),
        }