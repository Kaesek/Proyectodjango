# Generated by Django 4.2.1 on 2023-06-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0013_alter_postulante_vivienda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_perros',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
