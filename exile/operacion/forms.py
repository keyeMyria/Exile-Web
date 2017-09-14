# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
import models
import widgets
from exile.servicios import get_cuenta
from django.db.models import Q
from cuser.middleware import CuserMiddleware
from djcelery.models import PeriodicTask, CrontabSchedule

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
