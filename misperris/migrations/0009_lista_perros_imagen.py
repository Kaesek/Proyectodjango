# Generated by Django 4.2.1 on 2023-06-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0008_alter_postulante_vivienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista_perros',
            name='imagen',
            field=models.ImageField(default=2, upload_to='imagenes_perros_rescatados'),
            preserve_default=False,
        ),
    ]