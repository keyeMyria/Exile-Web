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
from django.db.models import Q

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
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
                cuenta__asistente=self.request.user.pk, eliminado=True) | Q(
                    cuenta__asistente=self.request.user.pk, eliminado=True))
        else:
            queryset = queryset.filter(Q(cuenta__cliente=self.request.user.pk, eliminado=False) | Q(
                cuenta__asistente=self.request.user.pk, eliminado=False) | Q(
                    cuenta__asistente=self.request.user.pk, eliminado=False))
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
    list_display = ['nombre', 'id', 'servicios']
    search_fields = ['nombre', ]
    paginate_by = 10

    def servicios(self, obj, row):
        edit = "/novedades/tipo/form/%d/" % (obj.id)
        delete = "/novedades/tipo/delete/%d/" % (obj.id)
        return {'add': '/novedades/tipo/form/', 'edit': edit, 'delete': delete}
    # end def
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
    list_display = ['id', 'nombre', 'tipoR', 'clienteR', 'lugarR', 'latitud', 'longitud',
                    'descripcion', 'creatorR', 'fecha', 'estado', 'servicios']
    search_fields = ['nombre', 'descripcion',
                     'tipo_nombre']
    model = models.Reporte
    paginate_by = 10

    def tipoR(self, obj, row):
        if obj.tipo:
            return {"nombre": obj.tipo.nombre, "id": obj.tipo.id }
        # end if
        return {}
    # end def

    def clienteR(self, obj, row):
        if obj.cliente:
            return {"nombre": obj.cliente.nombre, "id": obj.cliente.id}
        # end if
        return {}
    # end def

    def lugarR(self, obj, row):
        if obj.lugar:
            return {"nombre": obj.lugar.nombre, "id": obj.lugar.id}
        # end if
        return {}
    # end def

    def creatorR(self, obj, row):
        nombre = "%s %s" % (obj.creator.first_name, obj.creator.last_name)
        return {"username": obj.creator.username, "nombre": nombre}
    # end def

    def servicios(self, obj, row):
        edit = "/novedades/reporte/form/%d/" % (obj.id)
        delete = "/novedades/reporte/delete/%d/" % (obj.id)
        return {'add': '/novedades/reporte/form/', 'edit': edit, 'delete': delete}
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
    list_display = ['url', ]
    model = models.FotoReporte

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
