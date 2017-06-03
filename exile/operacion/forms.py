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
        exclude = ()
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


class TipoForm(forms.ModelForm):

    class Meta:
        model = models.Tipo
        fields = ['nombre', ]
    # end class

    def clean(self):
        if get_cuenta():
            return super(TipoForm, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no esta asociado a una cuenta")
    # end def

    def save(self, commit=False):
        tipo = super(TipoForm, self).save(commit)
        if get_cuenta():
            tipo.cuenta = get_cuenta()
            tipo.save()
        # end if
        return tipo
    # end def
# end class


class TipoFormEdit(forms.ModelForm):

    class Meta:
        model = models.Tipo
        fields = ['nombre', 'eliminado']
    # end class

    def save(self, commit=False):
        tipo = super(TipoFormEdit, self).save(commit)
        if tipo.eliminado:
            user = CuserMiddleware.get_user()
            if user:
                tipo.eliminado_por = user
            # end if
        # end if
        tipo.save()
        return tipo
# end class
