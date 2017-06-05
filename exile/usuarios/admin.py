# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
# Register your models here.


@admin.register(models.Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cuenta', 'nombre', 'fecha', 'creator', 'last_editor', 'eliminado', 'eliminado_por')
    search_fields = ('nombre', )
    list_filter = ('cuenta', 'creator', 'last_editor')
    icon = '<i class="material-icons">star_border</i>'
# end class


@admin.register(models.Empleado)
class Empleado(admin.ModelAdmin):
    list_display = ('cuenta', 'first_name', 'last_name', 'username', 'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'fijo', 'creator', 'last_editor', 'eliminado', 'eliminado_por', 'avatar')
    search_fields = ('first_name', 'last_name', 'username', 'identificacion', 'telefono')
    list_filter = ('cuenta', 'creator', 'last_editor')
    icon = '<i class="material-icons">person</i>'
# end class


@admin.register(models.Grupo)
class Grupo(admin.ModelAdmin):
    list_display = ('cuenta', 'nombre', 'creator', 'last_editor', 'eliminado', 'eliminado_por')
    search_fields = ('nombre', )
    list_filter = ('cuenta', 'creator', 'last_editor')
    filter_horizontal = ('empleados', )
    icon = '<i class="material-icons">group</i>'
# end class
