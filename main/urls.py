from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nuevocliente", views.cargar_cliente, name="nuevocliente"),
    path("nuevaorden", views.nueva_orden, name="nuevaorden"),
    path("ordenes", views.orden, name="ordenes"),
    path("contacto", views.contacto, name="contacto"),
    ]