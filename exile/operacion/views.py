# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from exile.decorator import check_login
from usuarios import models as usuarios
from supra import views as supra
from django.db.models import Q
import forms
import croniter
import models
import urllib2
import json
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = "http://192.168.1.24:4200"
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.body = True
# Create your views here.


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


class TipoSupraForm(supra.SupraFormView):
    model = models.Tipo
    form_class = forms.TipoForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TipoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class
