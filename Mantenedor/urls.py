# -*- coding: utf-8 -*-
"""Mantenedor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.utils.encoding import force_bytes

def __str__(self):
    return force_bytes(self.name)

from django.contrib import admin
from django.urls import path
from CRUD.views import menu, agregar, buscar,buscador_nombre, buscador_carrera

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu),
    path('agregar/', agregar),
    path('buscar/', buscar),
    path('buscador_nombre/', buscador_nombre),
    path('buscador_carrera/<int:id>/', buscador_carrera),
]
