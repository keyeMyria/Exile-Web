# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from cuser.middleware import CuserMiddleware
from django.http import HttpResponse
from exile.decorator import check_login, get_cuenta
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
from usuarios.views import UserDetail, EmpleadoList, GrupoList
from datetime import datetime

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
            return forms.TareaFormEdit
        # end if
        return forms.TareaForm
    # end class
# end class

class CrontabScheduleSupraForm(supra.SupraFormView):
    model = models.CrontabSchedule
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
    model = models.CrontabSchedule

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

class NotificacionList(supra.SupraListView):
    model = models.Notificacion
    list_display = [
     'id', ('tarea', 'json'), 'fecha', ('multimedia', 'json'), ('subnotificaciones', 'json'),
     'completado', 'latitud', 'longitud', ('lista_completados', 'json')
    ]
    list_filter = ['fecha']

    def get_queryset(self,):
        queryset = super(NotificacionList, self).get_queryset()
        fecha_inicio = self.request.GET.get('fecha_inicio', False)
        fecha_final = self.request.GET.get('fecha_final', False)
        esta_completado = self.request.GET.get('esta_completado', False)
        if fecha_inicio and fecha_final:
            queryset = queryset.filter(fecha__gte=fecha_inicio, fecha__lte=fecha_final)
        # end if
        if esta_completado:
            queryset = queryset.extra(where=["""(
                    SELECT NOT descompletado
                    FROM
                        operacion_completado
                    WHERE notificacion_id = operacion_notificacion.id
                    ORDER BY fecha DESC
                    LIMIT 1) = %s """], params=(esta_completado, ))
            print queryset.query
        # end if
        return queryset
    # end def

    def subnotificaciones(self, obj, row):
        class request():
            method = 'GET'
            GET = {'notificacion': obj.pk}
        # end class
        subtareas = SubNotificacionList(dict_only=True).dispatch(request=request())
        return json.dumps(subtareas['object_list'])
    # end class

    def tarea(self, obj, row):
        class request():
            method = 'GET'
            GET = {'pk': obj.tarea.pk}
            user = self.request.user
        # end class
        tareas = TareaList(dict_only=True).dispatch(request=request())
        if len(tareas['object_list']):
            return json.dumps(tareas['object_list'][0])
        # end if
        return 'null'
    # end def

    def lista_completados(self, obj, row):
        class request():
            method = 'GET'
            GET = {'notificacion': obj.pk}
        # end class
        completados = CompletadoList(dict_only=True).dispatch(request=request())
        return json.dumps(completados)
    # end def

    def multimedia(self, obj, row):
        class request():
            method = 'GET'
            GET = {'notificacion': obj.pk}
        # end class
        multimedia = MultimediaList(dict_only=True).dispatch(request=request())
        return json.dumps(multimedia['object_list'])
    # end def

    def completado(self, obj, row):
        return models.Completado.objects.filter(notificacion=obj, descompletado=False).count() > 0
    # end def
# end class

class SubNotificacionList(supra.SupraListView):
    model = models.SubNotificacion
    list_display = ['id' ,'fecha', 'notificacion', ('subtarea', 'json'), 'nombre', 'descripcion',
     'completado', ('lista_completados', 'json')
     ]
    list_filter = ['pk', 'notificacion']

    def subtarea(self, obj, row):
        class request():
            method = 'GET'
            GET = {'pk': obj.subtarea.pk}
            user = self.request.user
        # end class
        tareas = SubTareaList(dict_only=True).dispatch(request=request())
        if len(tareas['object_list']):
            return json.dumps(tareas['object_list'][0])
        # end if
        return 'null'
    # end def

    def lista_completados(self, obj, row):
        class request():
            method = 'GET'
            GET = {'subnotificacion': obj.pk}
        # end class
        completados = CompletadoSubList(dict_only=True).dispatch(request=request())
        return json.dumps({})
    # end def

    def completado(self, obj, row):
        return models.CompletadoSub.objects.filter(subnotificacion=obj, descompletado=False).count() > 0
    # end def
# end class

class TareaDetail(supra.SupraDetailView):
    model = models.Tarea
    list_display  = ['id', 'cuenta', 'nombre', 'descripcion', 'lugar', 'cliente', 'creator', 'last_editor', 'grupo', 'sub_complete', 'eliminado', 'eliminado_por',]
# end class

class TareasPeriodicasList(supra.SupraListView):
    model = models.Tarea

    def get_queryset(self):
        queryset = super(TareasPeriodicasList, self).get_queryset()
        class QueryList():
            def __init__(self, lista):
                self.lista = lista
            # end def

            def __iter__(self):
                for node in self.lista:
                    yield node
                # end for
            # end def

            def __getitem__(self, i):
                return self.lista[i]

            def count(self):
                return len(self.lista)
            # end def
        # end class

        fecha_inicio = self.request.GET.get('fecha_inicio', False)
        fecha_final = self.request.GET.get('fecha_final', False)
        if fecha_inicio and fecha_final:
            lista = forms.TareaFormBase.get_tareas_periodicas(datetime.strptime(fecha_inicio, "%Y-%m-%d"), datetime.strptime(fecha_final, "%Y-%m-%d"))
        else:
            lista = []
        # end if
        queryset = QueryList(lista=lista)
        return queryset
    # end def
# end class

class TareaList(MasterList):
    model = models.Tarea
    list_display = [
        'id', 'fecha_ejecucion', 'fecha_finalizacion', 'interval', 'crontab',
        'cuenta', 'nombre', 'descripcion', 'lugar', 'cliente', ('empleados', 'json'),
        ('creator', 'json'), ('last_editor', 'json'), ('grupo', 'json'), ('empleados_grupo', 'json'), 'sub_complete', 'eliminado',
        ('eliminado_por', 'json'), ('subtareas', 'json'), 'latitud', 'longitud'
    ]
    search_fields = ['nombre', 'direccion', ]
    list_filter = ['pk', ]
    paginate_by = 10

    def empleados(self, obj, row):
        class request():
            method = 'GET'
            GET = {'tarea': obj.pk}
            user = self.request.user
        # end class
        empleados = EmpleadoList(dict_only=True).dispatch(request=request())
        return json.dumps(empleados['object_list'])
    # end def

    def grupo(self, obj, row):
        class request():
            method = 'GET'
            GET = {'grupo': obj.grupo.pk}
            user = self.request.user
        # end class
        empleados = GrupoList(dict_only=True).dispatch(request=request())
        if len(empleados):
            return json.dumps(empleados['object_list'][0])
        # end if
        return "null"
    # end def

    def empleados_grupo(self, obj, row):
        class request():
            method = 'GET'
            GET = {'grupo': obj.grupo.pk}
            user = self.request.user
        # end class
        empleados = EmpleadoList(dict_only=True).dispatch(request=request())
        return json.dumps(empleados['object_list'])
    # end def

    def creator(self, obj, row):
        class request():
            method = 'GET'
        # end class
        creator = UserDetail(dict_only=True).dispatch(request=request(), pk=obj.creator.pk)
        return json.dumps(creator)
    # end def

    def eliminado_por(self, obj, row):
        class request():
            method = 'GET'
        # end class
        if obj.eliminado_por:
            eliminado_por = UserDetail(dict_only=True).dispatch(request=request(), pk=obj.eliminado_por.pk)
            return json.dumps(eliminado_por)
        # end if
        return "null"
    # end def

    def last_editor(self, obj, row):
        class request():
            method = 'GET'
        # end class
        last_editor = UserDetail(dict_only=True).dispatch(request=request(), pk=obj.last_editor.pk)
        return json.dumps(last_editor)
    # end def

    def subtareas(self, obj, row):
        class request():
            method = 'GET'
            GET = {'tarea': obj.pk}
        # end class
        subtareas = SubTareaList(dict_only=True).dispatch(request=request())
        return json.dumps(subtareas['object_list'])
    # end def

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
    list_display = [
     'id', 'tarea', 'tarea__nombre', 'nombre', 'descripcion', 'creator',
     'last_editor', 'eliminado', 'eliminado_por', 'latitud', 'longitud'
     ]
    search_fields = ['nombre', 'direccion']
    list_filter = ['tarea']
# end class

class CompletadoList(supra.SupraListView):
    model = models.Completado
    list_filter = ['pk', 'notificacion']
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

class CompletadoDetail(supra.SupraDetailView):
    model = models.Completado
    list_display  = ['id', 'notificacion', 'fecha', 'creator', 'last_editor', 'latitud', 'longitud']
# end class

class CompletadoDelete(supra.SupraDeleteView):
    model = models.Completado
    response_json = True

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CompletadoDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.descompletado = True
        user = CuserMiddleware.get_user()
        self.object.descompletado_por = user
        self.object.save()
        return HttpResponse(status=200)
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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.descompletado = True
        user = CuserMiddleware.get_user()
        self.object.descompletado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class

class CompletadoSubList(supra.SupraListView):
    model = models.CompletadoSub
    list_filter = ['pk', 'subnotificacion']
# end class

class MultimediaList(supra.SupraListView):
    model = models.Multimedia
    list_display = ['id', 'notificacion', 'url', 'tipo', 'fecha']
    list_filter = ['notificacion']

    def url(self, obj, row):
        if obj.archivo:
            return "http://104.236.33.228:8000/media/%s" % (obj.archivo)
        # end if
        return None
    # end if
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
