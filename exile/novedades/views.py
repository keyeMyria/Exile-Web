# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from supra import views as supra
import forms
import models
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from cuser.middleware import CuserMiddleware
from usuarios import models as usuarios
from exile.decorator import check_login

# Create your views here.


supra.SupraConf.ACCECC_CONTROL["allow"] = True


class TipoReporteListView(supra.SupraListView):
    list_filter = ('id', )
    list_display = ['nombre', 'id', ]
    model = models.TipoReporte

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(TipoReporteListView, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class TipoSupraForm(supra.SupraFormView):
    model = models.TipoReporte

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TipoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class FotoReporteInlineForm(supra.SupraInlineFormView):
    model = models.FotoReporte

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(FotoReporteInlineForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ReporteListView(supra.SupraListView):
    list_filter = ['tipo_de_reporte', 'emisor', 'id']
    list_display = ['id', 'nombre', 'tipo_n', 'nombreC', 'lugar__nombre', 'latitud', 'longitud', 'cliente', 'lugar', 'tipo_de_reporte',
                    'descripcion', 'user', 'fecha', 'estado', 'numero']
    search_fields = ['nombre', 'descripcion',
                     'tipo_de_reporte__nombre', 'numero']
    model = models.Reporte
    paginate_by = 10

    class Renderer:
        nombreC = 'cliente__nombre'
        tipo_n = 'tipo_de_reporte__nombre'
        creator = 'usuario__username'
    # end class

    def get_queryset(self):
        queryset = super(ReporteListView, self).get_queryset()
        # Aqui val el filtro por subscripción
        return queryset.order_by('estado', '-fecha')
    # end def

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(ReporteListView, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ReporteForm(supra.SupraFormView):
    model = models.Reporte
    form_class = forms.ReporteSupraForm
    inlines = [FotoReporteInlineForm]

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ReporteForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class FotoReporteForm(supra.SupraFormView):
    model = models.FotoReporte

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(FotoReporteForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class FotoReporteListView(supra.SupraListView):
    list_filter = ['id', 'reporte']
    list_display = ['url', ]
    model = models.FotoReporte

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(FotoReporteListView, self).dispatch(request, *args, **kwargs)
    # end def
# end class
