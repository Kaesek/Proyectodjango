from django.shortcuts import render, redirect
from .models import Postulante
from .models import Lista_perros
# Create your views here.
def home(request):
    perrosLista = Lista_perros.objects.all()
    return render(request, 'gestionPerros.html', {"perros": perrosLista})

def registrarPerros(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    raza_predominante = request.POST['raza_predominante']
    descripcion = request.POST['descripcion']
    imagen = request.FILES['imagen']
    estado = request.POST['estado']

    perros = Lista_perros.objects.create(
       codigo = codigo, nombre = nombre, raza_predominante=raza_predominante, descripcion=descripcion, imagen=imagen ,estado=estado
    )
    return redirect('gestionPerros')

def eliminarPerros(request, codigo):
    perros = Lista_perros.objects.get(codigo = codigo)
    perros.delete()
    return redirect('gestionPerros')

def edicionPerros(request, codigo):
    perros = Lista_perros.objects.get(codigo = codigo)
    return render(request, 'edicionPerros.html', {"perros": perros})

def editarPerros(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    raza_predominante = request.POST['raza_predominante']
    descripcion = request.POST['descripcion']
    estado = request.POST['estado']

    perros = Lista_perros.objects.get(codigo=codigo)
    perros.nombre = nombre
    perros.raza_predominante = raza_predominante
    perros.descripcion = descripcion
    perros.estado = estado
    perros.save()
    return redirect('gestionPerros')

def formulario(request):
    return render(request, 'formulario.html')


def formularioCarga(request):
    correo = request.POST['email']
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    fecha_nacimiento = request.POST['fecha_nacimiento']
    telefono = request.POST['contacto']
    region = request.POST['region']
    comuna = request.POST['comuna']
    vivienda = request. POST['tipo_vivienda']

    postulante = Postulante.objects.create(
       correo = correo, rut = rut, nombre = nombre, fecha_nacimiento = fecha_nacimiento, telefono = telefono, region = region, comuna = comuna, vivienda = vivienda
    )
    return redirect('/')


def gestionPerros(request):
    perro = Lista_perros.objects.all()
    return render(request, 'gestionPerros.html', {'perros': perro})


def index(request):
    return render(request, 'index.html')