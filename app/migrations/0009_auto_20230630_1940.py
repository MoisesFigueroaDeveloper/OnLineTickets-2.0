# Generated by Django 3.1.2 on 2023-06-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20230626_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='categoria',
            field=models.IntegerField(choices=[(0, 'Musica'), (1, 'Deporte'), (2, 'Teatro'), (3, 'Familia')]),
        ),
    ]