# Generated by Django 5.1.2 on 2024-11-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabacosAPP', '0005_rename_imagenestanco_marca_imagenmarca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cigarrillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('Industriales', 'Industriales'), ('De liar', 'De liar')], max_length=20)),
                ('precio', models.PositiveIntegerField()),
                ('imagenCig', models.URLField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('precio', models.PositiveIntegerField()),
                ('imagenPuro', models.URLField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]