from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader  import get_template
from django.shortcuts import render
from CRUD.models import Personas, Carrera

class Persona(object):#CONSTRUCTOR DEL OBJETO PERSONA

    def __init__(self, nombre, apellido, fecha_nacimiento, carrera):
        
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.carrera = carrera

def menu(request): #INGRESO A CRUD

    return render(request, 'contenido/menu.html') #PARAMETROS DEL RENDER: (REQUEST O PETICION, PLANTILLA, CONTEXTO)

def agregar(request):
    return render(request,'contenido/agregar.html')

def buscar(request):

    carreras = Carrera.objects.all()

    return render(request,'contenido/buscar.html',{"carreras":carreras})

def buscador_nombre(request):

    if request.POST["nombre"] and request.POST["apellido"]:

        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]

        resultado = Personas.objects.filter(nombre__icontains = nombre).filter(apellido__icontains = apellido)
        
        for r in resultado:
            id = r.carrera_id
            nombre_carrera = Carrera.objects.get(id__icontains = id)


        return render(request, 'contenido/resultado_buscador.html', {"resultado": resultado , "carrera":nombre_carrera})
    else:
        mensaje = "No se ha encontrado ningun resultado en la busqueda"
        return render(request, 'contenido/resultado_buscador.html', {"mensaje":mensaje})

def buscador_carrera(request,id):

    if id:

        resultado = Personas.objects.get(carrera_id__icontains = id)

        for r in resultado:
            id = r.carrera_id
            nombre_carrera = Carrera.objects.get(id__icontains = id)
        
        return render(request, 'contenido/resultado_buscador.html', {"resultado": resultado , "carrera":nombre_carrera})
    else:
        mensaje = "No se ha encontrado ningun resultado en la busqueda"
        return render(request, 'contenido/resultado_buscador.html', {"mensaje":mensaje})



"""
def buscar_nombre(request):

    if request.POST["nombre"]:

        #mensaje="Nombre buscado es: %r" %request.POST["nombre"]
        nombre_=request.POST["nombre"]

        nombre_retorno = Personas.objects.filter(nombre__icontains = nombre_)
        return render(request,"contenido/resultados_busqueda.html", {"nombre":nombre_retorno})

    else:
        mensaje = "No hay nada"
        return render( mensaje)

"""