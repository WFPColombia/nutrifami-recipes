# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_auto_20170814_2007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paso',
            options={'verbose_name_plural': ' Pasos'},
        ),
        migrations.AlterModelOptions(
            name='receta',
            options={'verbose_name_plural': '  Recetas'},
        ),
    ]
