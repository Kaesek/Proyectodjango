from django.db import models


# Create your models here.
class Postulante(models.Model):
    TIPO_VIVIENDA = [
        ('grande', 'Casa con patio Grande'),
        ('pequeño', 'Casa con Patio Pequeño'),
        ('notiene', 'Casa sin patio'),
        ('notiene1', 'Departamento'),
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
            ('rescatado', 'Rescatado'),
            ('disponible', 'Disponible'),
            ('adoptado', 'Adoptado'),
            ('revision', 'revision psiquiatrica')
        ]
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    raza_predominante = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='imagenes_perros')
    estado = models.CharField(choices=TIPO_ESTADO, max_length=1000)
    
    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.codigo)

