# Generated by Django 3.1.2 on 2023-06-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20230630_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
