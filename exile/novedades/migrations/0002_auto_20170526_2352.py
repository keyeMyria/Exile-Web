# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 23:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporte',
            name='resend',
        ),
        migrations.AlterField(
            model_name='reporte',
            name='tipo_de_reporte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novedades.TipoReporte'),
        ),
    ]
