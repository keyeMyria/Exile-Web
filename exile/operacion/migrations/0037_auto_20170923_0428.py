# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-23 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0036_auto_20170915_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='latitud',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='longitud',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]