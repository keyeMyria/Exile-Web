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
from djcelery.models import PeriodicTask, IntervalSchedule

def test_add(request):
    schedule, created = IntervalSchedule.objects.get_or_create(every=10, period='seconds')
    PeriodicTask.objects.get_or_create(
        interval=schedule,                  # we created this above.
        name='Importing contacts',          # simply describes this periodic task.
        task='periodic2', 
    )
    return HttpResponse("Ok")
# end def

supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = ORIGIN
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.ACCECC_CONTROL["methods"] = "POST, GET, PUT, DELETE ,OPTIONS"
supra.SupraConf.body = True

def calendar(request):

    start = request.GET.get('start', False)
    end = request.GET.get('end', False)
    novedad_select = request.GET.get('novedad_select', '0')

    dates = []
    now = datetime.now()

    if start and isinstance(start, unicode) and start.isdigit():
        start = datetime.fromtimestamp(int(start))
    else:
        try:
            parts = start.split('-')
            start = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
        except Exception as e:
            print "1 Error fetching date ", e
        # end try
    # end if
    if end and isinstance(end, unicode) and end.isdigit():
        end = datetime.fromtimestamp(int(end))
    else:
        try:
            parts = end.split('-')
            end = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
        except Exception as e:
            print "2 Error fetching date", e
        # end try
    # end if
    key = request.GET.get('key', False)
    empleado = request.GET.get('empleado', request.user.pk)
    if request.user.is_authenticated():
        empleado = usuarios.Empleado.objects.filter(pk=empleado).first()
    else:
        empleado = False
    # end if
    if start and end:
        if novedad_select == '0' or novedad_select == '1':
            dates = dates + activities(request, start, end, now, empleado)
        # end if
        if (novedad_select == '0' or novedad_select == '3') and not empleado:
            dates = dates + cumpleanios(request, start, end, now)
        # end if
    # end if
    return HttpResponse(json.dumps(dates, cls=DjangoJSONEncoder), content_type="application/json")
# end def


def cumpleanios(request, start, end, now):
    usuari = [usuarios.Asistente, usuarios.Empleado]
    dates = []
    for users in usuari:
        userlist = users.objects.all()
        for user in userlist:
            str_cron = "0 7 %s %s *" % (user.fecha_nacimiento.day,
                                        user.fecha_nacimiento.month)
            print str_cron
            cron = croniter.croniter(
                str_cron, datetime.combine(start, datetime.min.time()))
            nextdate = start
            while nextdate <= end:
                nextdate = cron.get_next(datetime)
                # end if
                dates.append({
                    'pk': user.pk,
                    'cron': str_cron,
                    'title': "Hoy cumple %s %s" % (user.first_name, user.last_name),
                    'now': now.strftime("%Y-%m-%d %I:%M%p"),
                    'start': nextdate.strftime("%Y-%m-%d"),
                    'urli': reverse('admin:%s_%s_change' % (user._meta.app_label,  user._meta.model_name),  args=[user.pk]),
                    "_send_to_": ['Gerente'],
                    'type': 'Cumple'
                })
            # end while
        # end if
    # end for
    return dates
# end def


def activities(request, start, end, now, empleado):
    acts = models.Tarea.objects.filter(
        fecha_de_ejecucion__gte=start, fecha_de_ejecucion__lte=end)

    lugar = request.GET.get('lugar', '0')

    if lugar != '0':
        acts = acts.filter(lugar=int(lugar))
    # end if

    cliente = request.GET.get('cliente', '0')
    if cliente != '0':
        acts = acts.filter(cliente=int(cliente))
    # end if
    if empleado:
        acts = acts.filter(Q(empleados=empleado) | Q(grupo__empleados=empleado))
    # end if
    dates = []
    for act in acts:
        if act.repetir_cada == 'no':
            dates.append({
                'pk': act.id,
                'title': "%s" % (act.nombre),
                'now': now.strftime("%Y-%m-%d %I:%M%p"),
                'start': act.fecha_de_ejecucion.strftime("%Y-%m-%d"),
                # "_send_to_": ['Piscinero'],
                'empleado': dict(act.empleados),
                'grupo': act.grupo,
                # "urli": reverse('admin:%s_%s_change' % (act._meta.app_label,  act._meta.model_name),  args=[act.pk]),
                'type': 'Tarea'
            })
        else:
            str_cron = get_cron(act)
            cron = croniter.croniter(str_cron, datetime.combine(
                act.fecha_de_ejecucion, datetime.min.time()))

            nextdate = start
            while nextdate <= end:
                nextdate = cron.get_next(datetime)
                dates.append({
                    'pk': act.id,
                    'cron': str_cron,
                    'title': "%s" % (act.nombre),
                    'now': now.strftime("%Y-%m-%d %I:%M%p"),
                    'start': nextdate.strftime("%Y-%m-%d"),
                    # "urli": reverse('admin:%s_%s_change' % (act._meta.app_label,  act._meta.model_name),  args=[act.pk]),
                    'empleado': dict(act.empleados),
                    'grupo': act.grupo,
                    'type': 'Tarea'
                })
            # end while
        # end if
    # end for
    return dates
# end def


def get_cron(instance):
    cron = ""
    if "dias[" in instance.repetir_cada:  # dias de la semana
        cron = "0 7 * * %s" % (instance.repetir_cada.replace(
            "dias[", "").replace("]", ""), )
    elif "mes[" in instance.repetir_cada:  # dias del mes
        cron = "0 7 %s * *" % (instance.repetir_cada.replace(
            "mes[", "").replace("]", ""), )
    else:
        if int(instance.repetir_cada) <= 0:
            instance.repetir_cada = '1'
            instance.save()
        # end if
        if instance.unidad_de_repeticion == 3:  # intervalo mensual
            cron = "0 7 %s */%s *" % ('%(dia)s', instance.repetir_cada, )
        elif instance.unidad_de_repeticion == 4:  # intervalo anual
            cron = "0 7 %s %s/%d *" % ('%(dia)s', '%(mes)s',
                                       int(instance.repetir_cada) * 12, )
        # end if
    return cron % {
        'dia': instance.fecha_de_ejecucion.day,
        'mes': instance.fecha_de_ejecucion.month,
        'dia_semana': instance.fecha_de_ejecucion.weekday()
    }
# end def


def error(request):
    return "error"
# end def


def connections(request):
    return HttpResponse("%s:%s" % (HOST, IO_PORT))
# end def


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
    list_display = ['id', 'cuenta', 'nombre', 'descripcion', 'fecha_de_ejecucion', 'repetir_cada', 'lugar', 'cliente', 'empleados', 'creator', 'last_editor', 'grupo', 'sub_complete', 'unidad_de_repeticion', 'eliminado', 'eliminado_por', 'completado', ('subtareas', 'json'), ('multimedia', 'json')]
    search_fields = ['nombre', 'direccion', ]
    paginate_by = 10

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
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CompletadoDelete, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class MultimediaList(supra.SupraListView):
    model = models.Multimedia
    list_display = ['tarea', 'url', 'audio', 'foto']
    list_filter = ['tarea']
    paginate_by = 10

    def url(self, obj, row):
        if obj.archivo:
            return "/media/%s" % (obj.archivo)
        # end if
        return None
    # end if
# end class

class MultimediaSupraForm(supra.SupraFormView):
    model = models.Multimedia
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(MultimediaSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class MultimediaDeleteSupra(supra.SupraDeleteView):
    model = models.Multimedia
    response_json = False

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(MultimediaDelete, self).dispatch(request, *args, **kwargs)
    # end def
# end class
