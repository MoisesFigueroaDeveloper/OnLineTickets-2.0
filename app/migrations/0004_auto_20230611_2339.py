# Generated by Django 3.1.2 on 2023-06-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_eventos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactanos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_cosultas', models.IntegerField(choices=[[0, 'consultas'], [1, 'reclamos'], [2, 'suguerencias'], [3, 'Felicitaciones']])),
                ('mensaje', models.TextField(max_length=250)),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
    ]
