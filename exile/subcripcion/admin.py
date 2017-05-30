# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
import models
import forms
# Register your models here.

class ModuloAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion', 'estado']
    search_fields = ['nombre','descripcion']
    form = forms.ModuloForm

    def get_queryset(self, request):
        queryset = super(ModuloAdmin, self).get_queryset(request)
        return queryset.order_by('estado')
    # end def
#end class


class FuncionalidadAdmin(admin.ModelAdmin):
    list_display = ['modulo','nombre','descripcion','url', 'estado']
    search_fields = ['nombre','descripcion']
    form = forms.FuncionalidadForm

    def get_queryset(self, request):
        queryset = super(FuncionalidadAdmin, self).get_queryset(request)
        return queryset.order_by('modulo','nombre','estado')
    # end def
#end class


class InstModuloAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','modulo', 'estado']
    search_fields = ['nombre','descripcion']
    filter_horizontal = ['funcionalidades']
    form = forms.InstModuloForm

    def get_queryset(self, request):
        queryset = super(InstModuloAdmin, self).get_queryset(request)
        return queryset.order_by('modulo','nombre','estado')
    # end def
#end class


class PlanAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'operadores', 'asistentes', 'descripcion', 'valor', 'duracion', 'estado']
    search_fields = ['nombre','descripcion', 'operadores', 'asistentes', 'valor', 'duracion']
    filter_horizontal = ['modulos']
    form = forms.PlanForm

    def get_queryset(self, request):
        queryset = super(PlanAdmin, self).get_queryset(request)
        return queryset.order_by('nombre', 'duracion','estado')
    # end def
#end class


admin.site.register(models.Funcionalidad)
admin.site.register(models.Modulo, ModuloAdmin)
admin.site.register(models.InstModulo, InstModuloAdmin)
admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.Suscripcion)
admin.site.register(models.Factura)
admin.site.register(models.Cuenta)
