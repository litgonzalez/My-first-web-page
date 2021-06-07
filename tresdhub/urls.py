from django.contrib import admin
from django.urls import path, include
from main.views import index

urlpatterns = [
    path("", index, name="index"),
    path('admin/', admin.site.urls),
    path('main/', include("main.urls"))
]
