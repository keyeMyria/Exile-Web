# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0011_auto_20170601_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='suscripciones',
        ),
        migrations.AddField(
            model_name='suscripcion',
            name='cuenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subcripcion.Cuenta'),
            preserve_default=False,
        ),
    ]
