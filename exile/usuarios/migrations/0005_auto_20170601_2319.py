# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 23:19
from __future__ import unicode_literals

import cuser.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0004_usuario_eliminado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='creator',
            field=cuser.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_cargo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cargo',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cargo',
            name='eliminado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eliminado_cargo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cargo',
            name='last_editor',
            field=cuser.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_edited_cargo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuario',
            name='eliminado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eliminado_por_usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
