# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 15:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0006_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Me gusta', 'Me gusta'), ('Compartir', 'Compartir')], max_length=80)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': ' Interacciones',
            },
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Las imagenes deben tener un tama\xf1o de 386x249 pixeles', null=True, upload_to='recetas'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Determina si la receta es visible en la app o no', verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interaction',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to='recetas.Receta'),
        ),
    ]
