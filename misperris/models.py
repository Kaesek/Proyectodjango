from django.db import models

# Create your models here.
class Postulante(models.Model):
    TIPO_VIVIENDA = [
        (1, 'Casa con patio Grande'),
        (2, 'Casa con Patio Pequeño'),
        (3, 'Casa sin patio'),
        (4, 'Departamento'),
    ]
    correo = models.EmailField(max_length=30)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    vivienda = models.CharField(choices=TIPO_VIVIENDA, max_length=1000)

    def __str__(self):
        text = "{0}"
        return text.format(self.nombre)
    
class Lista_perros(models.Model):
    TIPO_ESTADO = [
            (1, 'Rescatado'),
            (2, 'Disponible'),
            (3, 'Adoptado'),
        ]
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100)
    raza_predominante = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    estado = models.CharField(choices=TIPO_ESTADO, max_length=5)
    
    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.codigo)

 