# Generated by Django 5.1.3 on 2024-12-04 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabacosAPP', '0010_distribuidor_imagendistr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribuidor',
            name='imagenDistr',
        ),
    ]