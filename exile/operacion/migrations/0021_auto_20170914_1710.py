# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-14 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djcelery', '0001_initial'),
        ('operacion', '0020_tarea_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='crontab',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djcelery.CrontabSchedule'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='cron_ejecucion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ejecucion', to='djcelery.CrontabSchedule'),
        )
    ]
