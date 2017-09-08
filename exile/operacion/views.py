# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from cuser.middleware import CuserMiddleware
from django.http import HttpResponse
from exile.decorator import check_login
from usuarios import models as usuarios
from supra import views as supra
from django.db.models import Q
import forms
import croniter
import models
import urllib2
import json
from exile.settings import ORIGIN
from djcelery.models import CrontabSchedule, IntervalSchedule
from django.contrib.sites.models import Site

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
    model = models.Tipo
    form_class = forms.TipoForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TipoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.TipoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class TipoDeleteSupra(supra.SupraDeleteView):
    model = models.Tipo

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
    model = models.Tipo
    list_display = ['nombre', 'id']
    search_fields = ['nombre', ]
    paginate_by = 10
# end class


class ClienteSupraForm(supra.SupraFormView):
    model = models.Cliente
    form_class = forms.ClienteForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ClienteSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.ClienteFormEdit
        # end if
        return self.form_class
    # end class
# end class


class ClienteDeleteSupra(supra.SupraDeleteView):
    model = models.Cliente

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ClienteDeleteSupra, self).dispatch(request, *args, **kwargs)
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


class ClienteList(MasterList):
    model = models.Cliente
    list_display = ['nombre', 'id', 'tipo__nombre', 'tipo', 'identificacion', 'direccion', 'telefono']
    search_fields = ['nombre', 'identificacion', 'telefono', 'direccion']
    list_filter = ['tipo', ]
    paginate_by = 10
# end class


class LugarSupraForm(supra.SupraFormView):
    model = models.Lugar
    form_class = forms.LugarForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LugarSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.LugarFormEdit
        # end if
        return self.form_class
    # end class
# end class


class LugarDeleteSupra(supra.SupraDeleteView):
    model = models.Lugar

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LugarDeleteSupra, self).dispatch(request, *args, **kwargs)
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

class LugarList(MasterList):
    model = models.Lugar
    list_display = ['nombre', 'id', 'direccion', 'latitud', 'longitud', 'eliminado']
    search_fields = ['nombre', 'direccion', ]
    paginate_by = 10
# end class

class TareaSupraForm(supra.SupraFormView):
    model = models.Tarea
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TareaSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.TareaFormEdit
        # end if
        return forms.TareaForm
    # end class
# end class

class CrontabScheduleSupraForm(supra.SupraFormView):
    model = models.CrontabDateSchedule
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CrontabScheduleSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class IntervalScheduleSupraForm(supra.SupraFormView):
    model = models.IntervalSchedule
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(IntervalScheduleSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class IntervalScheduleDeleteSupra(supra.SupraDeleteView):
    model = models.Tarea

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(IntervalScheduleDeleteSupra, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class CrontabScheduleDeleteSupra(supra.SupraDeleteView):
    model = models.Tarea

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CrontabScheduleDeleteSupra, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class TareaDeleteSupra(supra.SupraDeleteView):
    model = models.Tarea

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TareaDeleteSupra, self).dispatch(request, *args, **kwargs)
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

class TareaList(MasterList):
    model = models.Tarea
    list_display = ['id', 'cuenta', 'nombre', 'descripcion', 'lugar', 'cliente', ('empleados', 'json'), 'creator', 'last_editor', 'grupo', 'sub_complete', 'eliminado', 'eliminado_por', 'completado', ('subtareas', 'json'), ('multimedia', 'json')]
    search_fields = ['nombre', 'direccion', ]
    paginate_by = 10

    def empleados(self, obj, row):
        lista = []
        empleados = usuarios.Empleado.objects.filter(tarea=obj).values('id')
        for e in empleados:
            lista.append(e['id'])
        return json.dumps(lista)
    # end def

    def completado(self, obj, row):
        completado = models.Completado.objects.filter(tarea=obj).first()
        if completado:
            return completado.pk
        # end if
    # end def

    def subtareas(self, obj, row):
        class request():
            method = 'GET'
            GET = {'tarea': obj.pk}
        # end class
        subtareas = SubTareaList(dict_only=True).dispatch(request=request())
        return json.dumps(subtareas['object_list'])
    # end def

    def multimedia(self, obj, row):
        class request():
            method = 'GET'
            GET = {'tarea': obj.pk}
        # end class
        multimedia = MultimediaList(dict_only=True).dispatch(request=request())
        return json.dumps(multimedia['object_list'])
# end class

class SubTareaSupraForm(supra.SupraFormView):
    model = models.SubTarea
    form_class = forms.SubTareaForm
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SubTareaSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.TipoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class SubTareaDeleteSupra(supra.SupraDeleteView):
    model = models.SubTarea

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SubTareaDeleteSupra, self).dispatch(request, *args, **kwargs)
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

class SubTareaList(supra.SupraListView):
    model = models.SubTarea
    list_display = ['id', 'tarea', 'tarea__nombre', 'nombre', 'descripcion', 'creator', 'last_editor', 'eliminado', 'eliminado_por', 'completado']
    search_fields = ['nombre', 'direccion']
    list_filter = ['tarea']


    def completado(self, obj, row):
        completado = models.CompletadoSub.objects.filter(subtarea=obj).first()
        if completado:
            return completado.pk
        # end if
    # end def
# end class

class CompletadoSubForm(supra.SupraFormView):
    model = models.CompletadoSub

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CompletadoSubForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class CompletadoSubDelete(supra.SupraDeleteView):
    model = models.CompletadoSub
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CompletadoSubDelete, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class CompletadoForm(supra.SupraFormView):
    model = models.Completado
    response_json = True

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CompletadoForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class CompletadoDelete(supra.SupraDeleteView):
    model = models.Completado
    response_json = True

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CompletadoDelete, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class MultimediaList(supra.SupraListView):
    model = models.Multimedia
    list_display = ['id', 'tarea', 'url', 'tipo']
    list_filter = ['tarea']
    paginate_by = 10

    def url(self, obj, row):
        if obj.archivo:
            return "http://104.236.33.228:8000/media/%s" % (obj.archivo)
        # end if
        return None
    # end if

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(MultimediaList, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class MultimediaSupraForm(supra.SupraFormView):
    model = models.Multimedia
    form_class = forms.MultimediaForm
    response_json = True

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(MultimediaSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class MultimediaDeleteSupra(supra.SupraDeleteView):
    model = models.Multimedia
    response_json = True

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(MultimediaDeleteSupra, self).dispatch(request, *args, **kwargs)
    # end def


    def delete(self, request, *args, **kwargs):
        self.get_object().archivo.delete()
        return super(MultimediaDeleteSupra, self).delete(request, *args, **kwargs)
    # end def
# end class
