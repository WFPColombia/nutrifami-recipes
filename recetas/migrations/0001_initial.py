# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 19:44
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Implemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripci\xf3n')),
            ],
            options={
                'verbose_name_plural': 'Implementos',
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre como es conocido com\xfanmente el ingrediente', max_length=200)),
                ('nombre2', models.CharField(blank=True, help_text='Otro nombre con el que pueda ser reconocido el alimento', max_length=200, null=True, verbose_name='otros nombres')),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('unidad', models.CharField(choices=[('Kilogramos', 'Kilogramos'), ('Gramos', 'Gramos'), ('Unidades', 'Unidades'), ('Tazas', 'Tazas'), ('Cucharadas', 'Cucharadas')], max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Ingredientes',
            },
        ),
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.PositiveSmallIntegerField(help_text='Orden del paso seg\xfan la receta')),
                ('paso', ckeditor.fields.RichTextField(help_text='Pasos para realizar la receta', verbose_name='Preparaci\xf3n')),
            ],
            options={
                'verbose_name_plural': 'Implementos',
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la receta', max_length=200)),
                ('imagen', models.ImageField(blank=True, help_text='Las imagenes deben tener un tama\xf1o de 400x120 pixeles', null=True, upload_to='recetas')),
                ('region', models.CharField(help_text='Regi\xf3n de donde es la receta', max_length=45, verbose_name='Regi\xf3n')),
                ('porciones', models.PositiveSmallIntegerField(help_text='La cantidad de porciones finales de la receta.')),
                ('tiempo_preparacion', models.CharField(help_text='Duraci\xf3n de preparacion de la receta en minutos', max_length=45, verbose_name='Tiempo de preparaci\xf3n')),
                ('sugerencia', models.TextField(blank=True, help_text='Sugerencia en la elaboraci\xf3n de la receta para los lectores', null=True)),
                ('is_active', models.BooleanField(default=False, help_text='Determina si el proyecto es visible en la app o no', verbose_name='Activo')),
                ('implementos', models.ManyToManyField(help_text='Implementos utilisados en la elaboraci\xf3n de la receta', to='recetas.Implemento')),
                ('ingredientes', models.ManyToManyField(to='recetas.Ingrediente')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to=settings.AUTH_USER_MODEL)),
                ('pasos', models.ForeignKey(help_text='Pasos para realizar la receta', on_delete=django.db.models.deletion.CASCADE, to='recetas.Paso', verbose_name='Pasos de la receta')),
            ],
            options={
                'verbose_name_plural': ' Recetas',
            },
        ),
    ]
