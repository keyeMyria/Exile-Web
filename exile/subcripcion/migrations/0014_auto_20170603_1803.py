# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0013_auto_20170603_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subcripcion.Cuenta'),
        ),
    ]
