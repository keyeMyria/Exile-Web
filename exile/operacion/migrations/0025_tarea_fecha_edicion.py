# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-14 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0024_auto_20170914_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_edicion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
