# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-14 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0027_auto_20170914_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completadosub',
            name='subtarea',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operacion.SubNotificacion'),
        ),
    ]
