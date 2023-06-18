# Generated by Django 4.2.1 on 2023-05-27 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0004_rename_listaperros_lista_perros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_perros',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Rescatado'), (2, 'Disponible'), (3, 'Adoptado')], max_length=5),
        ),
    ]
