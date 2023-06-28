from django.shortcuts import render, redirect
from .models import Postulante
from .models import Lista_perros
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CreacionUsuarioCustom


# Create your views here.
def register(request):
    data = {
        'form': CreacionUsuarioCustom()
    }

    if request.method == 'POST':
        user_creation_form = CreacionUsuarioCustom(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
    return render(request, 'registration/register.html', data)

def success(request):
    return render(request, 'misperris/success.html')
@login_required
def gestionPerros(request):
    perro = Lista_perros.objects.all()
    return render(request, 'misperris/gestionPerros.html', {'perros': perro})

def exit(request):
    logout(request)
    return redirect('index')
#@login_required
#def admin_view(request):
    #if request.user is not None:
     #   if(request.user.is_superuser):
      #      lista = Lista_perros.objects.all()
       #     context = {'lista': lista}
        #    return render(request, 'gestionPerros.html', context)
        #else:
         #   return render(request, 'login.html')
    #else:
     #   return render(request, 'login.html')   #

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
    return render(request, 'misperris/edicionPerros.html', {"perros": perros})


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
    return render(request, 'misperris/formulario.html')

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
    return redirect('success')


def index(request):
    return render(request, 'misperris/index.html')

