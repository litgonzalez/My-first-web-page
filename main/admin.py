from django.contrib import admin

# Register your models here.
from main import models

my_models = [models.Persona, models.Categoria, models.Producto, models.Orden_compra]
admin.site.register(my_models)