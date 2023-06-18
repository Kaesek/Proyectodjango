# Generated by Django 4.2.1 on 2023-05-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0002_alter_postulante_rut_alter_postulante_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='listaPerros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('raza_predominante', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('estado', models.IntegerField(choices=[(1, 'Rescatado'), (2, 'Disponible'), (3, 'Adoptado')])),
            ],
        ),
    ]