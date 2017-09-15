# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
import models
import widgets
from exile.servicios import get_cuenta
from django.db.models import Q
from cuser.middleware import CuserMiddleware
from djcelery.models import PeriodicTask, CrontabSchedule
from datetime import timedelta

class Master(forms.ModelForm):

    def clean(self):
        if get_cuenta():
            return super(Master, self).clean()
        # end if
        raise forms.ValidationError("Este usuario no esta asociado a una cuenta")
    # end def

    def save(self, commit=False):
        master = super(Master, self).save(commit)
        if get_cuenta():
            master.cuenta = get_cuenta()
            master.save()
        # end if
        return master
    # end def
# end class


class MasterEdit(forms.ModelForm):

    def save(self, commit=False):
        master = super(MasterEdit, self).save(commit)
        if master.eliminado:
            user = CuserMiddleware.get_user()
            if user:
                master.eliminado_por = user
            # end if
        # end if
        master.save()
        return master
    # end def
# end class

class TareaFormBase(forms.ModelForm):

    class Meta:
        model = models.Tarea
        exclude = []
    # end class

    @staticmethod
    def get_tareas_periodicas(fecha_inicio, fecha_final):
        fecha = fecha_inicio
        tareas = []
        while fecha < fecha_final:
            crons = models.Tarea.objects.filter(
                Q(crontab__day_of_month='*') | Q(crontab__day_of_month=fecha.day),
                Q(crontab__month_of_year='*') | Q(crontab__month_of_year=fecha.month),
                Q(fecha_ejecucion__lte=fecha)
            )

            strfecha = fecha.strftime("%Y-%m-%d")

            sql = """SELECT
                    *, '%(fecha)s'::date - tarea.fecha_ejecucion::date as _day_
                    FROM operacion_tarea as tarea
                    JOIN djcelery_intervalschedule as inte
                    ON 
                        tarea.interval_id = inte.id
                    AND
                        tarea.fecha_ejecucion <= '%(fecha)s'
                    AND (
                        CASE 
                            WHEN inte.period = 'days' THEN
                                '%(fecha)s'::date - tarea.fecha_ejecucion::date
                            WHEN inte.period = 'weeks' THEN
                                ('%(fecha)s'::date - tarea.fecha_ejecucion::date)/7
                            WHEN inte.period = 'months' THEN
                                date_part('months', age(' %(fecha)s', tarea.fecha_ejecucion)) +
                                date_part('years', age(' %(fecha)s', tarea.fecha_ejecucion))*12
                            WHEN inte.period = 'year' THEN
                                date_part('years', age(' %(fecha)s', tarea.fecha_ejecucion))
                        END
                    )::int %(percent)s inte.every = 0""" % {
                    'fecha': strfecha,
                    'percent': '%%'
                    } 

            intervals = models.Tarea.objects.raw(
                sql
            )
            for cron in crons:
                row = cron.__dict__
                row['pk'] = cron.pk
                row['__fecha__'] = strfecha
                tareas.append(row)
            # end for
            for interval in intervals:
                row = interval.__dict__
                row['pk'] = interval.pk
                row['__fecha__'] = strfecha
                tareas.append(row)
            # end for
            fecha = fecha + timedelta(days=1)
        # end for
        return tareas
    # end def
# end class

class MultimediaForm(forms.ModelForm):

    suport = {
        models.Multimedia.FOTO: ['jpg', 'png'],
        models.Multimedia.AUDIO: ['3gp', 'aac']
    }

    class Meta:
        model = models.Multimedia
        exclude = []
    # end class

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo', False)
        if archivo:
            if hasattr(archivo, '_size') and archivo._size > 25 * 1024 * 1024:
                raise forms.ValidationError("El tamaño de la archivo no puede ser superior a 25 mega")
            # end if
            tipo = self.cleaned_data.get('tipo', False)
            print 'tipo', tipo
            if tipo:
                ext = archivo.name.split('.')[1]
                if not ext.lower() in self.suport[tipo]:
                    raise forms.ValidationError(u'Unsupported file extension.')
                # end if
            # end if
            return archivo
        # end if
    # end def
# end class

class TareaForm(TareaFormBase):
    def save(self, commit=True):
        obj = super(TareaForm, self).save(commit=True)
        months = (obj.fecha_ejecucion.year - obj.fecha_edicion.year) * 12 + obj.fecha_ejecucion.month - obj.fecha_edicion.month
        crontab = CrontabSchedule.objects.create(
            minute = '0',
            hour = '7',
            day_of_week = '*',
            day_of_month = '%d' % (obj.fecha_ejecucion.day, ),
            month_of_year = '*/%d' % (months, )
        )
        obj.cron_ejecucion = PeriodicTask.objects.create(
            crontab = crontab,
            name = 'Tarea #%d' % (obj.pk, ),
            task = 'ejecutar',
            args = [obj.pk],
            expires = obj.fecha_ejecucion
        )
        obj.save()
        return obj
    # end def
# end class

class TareaFormEdit(TareaFormBase, MasterEdit):
    def save(self, commit=True):
        obj = super(TareaFormEdit, self).save(commit=True)
        months = (obj.fecha_ejecucion.year - obj.fecha_edicion.year) * 12 + obj.fecha_ejecucion.month - obj.fecha_edicion.month
        
        CrontabSchedule.objects.filter(pk=obj.cron_ejecucion.crontab.pk).update(
            minute = '0',
            hour = '7',
            day_of_week = '*',
            day_of_month = '%d' % (obj.fecha_ejecucion.day, ),
            month_of_year = '*/%d' % (months, )
        )
        PeriodicTask.objects.filter(pk=obj.cron_ejecucion.pk).update(
            name = 'Tarea #%d' % (obj.pk, ),
            task = 'ejecutar',
            args = [obj.pk],
            expires = obj.fecha_ejecucion
        )

        return obj
    # end def
# end class

class SubTareaFormBase(forms.ModelForm):

    class Meta:
        model = models.SubTarea
        fields = ['tarea', 'nombre', 'descripcion'] 
    # end class

# end class

class SubTareaForm(SubTareaFormBase, Master):
    pass
# end class

class SubTareaFormEdit(SubTareaFormBase, MasterEdit):
    pass
# end class

class TipoForm(Master):

    class Meta:
        model = models.Tipo
        fields = ['nombre', ]
    # end class
# end class


class TipoFormEdit(MasterEdit):

    class Meta:
        model = models.Tipo
        fields = ['nombre', 'eliminado']
    # end class
# end class


class ClienteForm(Master):

    class Meta:
        model = models.Cliente
        fields = ['nombre', 'tipo', 'identificacion', 'direccion', 'telefono']
    # end class
# end class


class ClienteFormEdit(MasterEdit):

    class Meta:
        model = models.Cliente
        fields = ['nombre', 'tipo', 'identificacion', 'direccion', 'telefono', 'eliminado']
    # end class
# end class


class LugarForm(Master):

    class Meta:
        model = models.Lugar
        fields = ['nombre', 'direccion', 'latitud', 'longitud']
    # end class
# end class


class LugarFormEdit(MasterEdit):

    class Meta:
        model = models.Lugar
        fields = ['nombre', 'direccion', 'latitud', 'longitud', 'eliminado']
    # end class
# end class
