# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
import models
import widgets
from exile.servicios import get_cuenta
from django.db.models import Q
from cuser.middleware import CuserMiddleware


class TareaForm(forms.ModelForm):

    class Meta:
        model = models.Tarea
        fields = ['nombre', 'descripcion', 'fecha_de_ejecucion', 'repetir_cada', 'unidad_de_repeticion','lugar', 'cliente', 'empleados', 'grupo', 'sub_complete']
        widgets = {
            # "fecha_de_ejecucion": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y"),
            "repetir_cada": widgets.IntervalWidget()
        }
    # end class

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_de_ejecucion'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['unidad_de_repeticion'].widgets = widgets.RepeatWidget(
            choices=self.fields['unidad_de_repeticion'].choices)
    # end def
# end class

class SubTareaForm(forms.ModelForm):

    class Meta:
        model = models.SubTarea
        fields = ['tarea', 'nombre', 'descripcion', 'creator', 'last_editor', 'eliminado', 'eliminado_por']
        widgets = {
            # "fecha_de_ejecucion": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y"),
            "repetir_cada": widgets.IntervalWidget()
        }
    # end class

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_de_ejecucion'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['unidad_de_repeticion'].widgets = widgets.RepeatWidget(
            choices=self.fields['unidad_de_repeticion'].choices)
    # end def
# end class


class Master(forms.ModelForm):

    def clean(self):
        if get_cuenta():
            return super(Master, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
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
