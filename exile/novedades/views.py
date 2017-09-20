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
from exile.decorator import check_login, get_cuenta
from exile.settings import ORIGIN
from django.db.models import Q

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True
supra.SupraListView.datetime_format = '%m/%d/%Y %I:%M %p'
supra.SupraListView.date_format = '%m/%d/%Y'

class MasterList(supra.SupraListView):
    search_key = 'q'

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(MasterList, self).dispatch(request, *args, **kwargs)
    # end def

    @method_decorator(get_cuenta)
    def get_queryset(self, cuenta):
        queryset = super(MasterList, self).get_queryset()
        if self.request.GET.get('num_page', False):
            self.paginate_by = self.request.GET.get('num_page', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        eliminado = self.request.GET.get('eliminado', False)
        if eliminado == '1':
            if cuenta:
                queryset = queryset.filter(cuenta=cuenta.id, eliminado=True)
        else:
            if cuenta:
                queryset = queryset.filter(cuenta=cuenta.id, eliminado=False)
        # end if
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
    response_json = False

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
    list_display = ['nombre', 'id',]
    search_fields = ['nombre', ]
    paginate_by = 10

# end class


class FotoReporteInlineForm(supra.SupraInlineFormView):
    model = models.FotoReporte
    response_json = False

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(FotoReporteInlineForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ReporteListView(MasterList):
    list_filter = ['tipo', 'cliente', 'lugar', 'id', 'estado']
    list_display = ['id', 'nombre', 'tipo', 'tipo__nombre', 'cliente', 'cliente__nombre','lugar', 'lugar__nombre',
                    'latitud', 'longitud', 'descripcion', 'creatorR', 'fecha', 'estado']
    search_fields = ['nombre', 'descripcion',
                     'tipo_nombre']
    model = models.Reporte
    paginate_by = 10

    def creatorR(self, obj, row):
        nombre = "%s %s" % (obj.creator.first_name, obj.creator.last_name)
        return {"username": obj.creator.username, "nombre": nombre}
    # end def
# end class


class ReporteForm(supra.SupraFormView):
    model = models.Reporte
    form_class = forms.ReporteSupraForm
    inlines = [FotoReporteInlineForm]
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ReporteForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.ReporteSupraFormEdit
        # end if
        return self.form_class
    # end class
# end class


class FotoReporteForm(supra.SupraFormView):
    model = models.FotoReporte
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(FotoReporteForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class FotoReporteListView(supra.SupraListView):
    list_filter = ['id', 'reporte']
    list_display = ['id', 'url', 'reporte']
    model = models.FotoReporte

    def url(self, obj, row):
        if obj.archivo:
            return "http://104.236.33.228:8000/media/%s" % (obj.foto)
        # end if
        return None
    # end if
    
    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(FotoReporteListView, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ReporteDeleteSupra(supra.SupraDeleteView):
    model = models.Reporte

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ReporteDeleteSupra, self).dispatch(request, *args, **kwargs)
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
