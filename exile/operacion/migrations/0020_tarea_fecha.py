# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-12 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0019_tarea_fecha_finalizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]