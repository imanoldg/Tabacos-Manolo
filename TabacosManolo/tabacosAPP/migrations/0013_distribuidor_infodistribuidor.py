# Generated by Django 5.1.3 on 2024-12-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabacosAPP', '0012_distribuidor_imagendistr'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribuidor',
            name='infoDistribuidor',
            field=models.CharField(default=False, max_length=2000),
        ),
    ]
