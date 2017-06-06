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
from exile.settings import ORIGIN

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.body = True


class MasterList(supra.SupraListView):
    search_key = 'q'

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(MasterList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(MasterList, self).get_queryset()
        if self.request.GET.get('num_page', False):
            self.paginate_by = self.request.GET.get('num_page', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        eliminado = self.request.GET.get('eliminado', False)
        if eliminado == '1':
            queryset = queryset.filter(Q(cuenta__cliente=self.request.user.pk, eliminado=True) | Q(
                cuenta__usuario=self.request.user.pk, eliminado=True))
        else:
            queryset = queryset.filter(Q(cuenta__cliente=self.request.user.pk, eliminado=False) | Q(
                cuenta__usuario=self.request.user.pk, eliminado=False))
            print queryset.count()
        if propiedad and orden:
            if orden == "asc":
                queryset = queryset.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-" + propiedad
                queryset = queryset.order_by(propiedad)
        # end if
        return queryset
    # end def
# end class


class TipoSupraForm(supra.SupraFormView):
    model = models.TipoReporte
    form_class = forms.TipoReporteForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TipoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.TipoReportFormEdit
        # end if
        return self.form_class
    # end class
# end class


class TipoDeleteSupra(supra.SupraDeleteView):
    model = models.TipoReporte

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TipoDeleteSupra, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class TipoList(MasterList):
    model = models.TipoReporte
    list_display = ['nombre', 'servicios']
    search_fields = ['nombre', ]
    paginate_by = 10

    def servicios(self, obj, row):
        edit = "/operacion/tipo/form/%d/" % (obj.id)
        delete = "/operacion/tipo/delete/%d/" % (obj.id)
        return {'add': '/operacion/tipo/form/', 'edit': edit, 'delete': delete}
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
    body = True

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ReporteForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class FotoReporteForm(supra.SupraFormView):
    model = models.FotoReporte
    body = True

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
