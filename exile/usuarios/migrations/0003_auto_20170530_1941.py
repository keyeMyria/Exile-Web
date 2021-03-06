# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0007_auto_20170530_1923'),
        ('usuarios', '0002_auto_20170525_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='cuenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subcripcion.Cuenta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo',
            name='cuenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subcripcion.Cuenta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='cuenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subcripcion.Cuenta'),
            preserve_default=False,
        ),
    ]
