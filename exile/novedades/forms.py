# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
import models
from exile.servicios import get_cuenta


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


class TipoReporteForm(Master):

    class Meta:
        model = models.TipoReporte
        fields = ['nombre', ]
    # end class
# end class


class TipoReportFormEdit(MasterEdit):

    class Meta:
        model = models.TipoReporte
        fields = ['nombre', 'eliminado']
    # end class
# end class


class ReporteSupraForm(Master):

    class Meta:
        model = models.Reporte
        fields = ['nombre', 'descripcion', 'tipo', 'cliente', 'lugar', 'latitud', 'longitud']
    # end class
# end class


class ReporteSupraFormEdit(MasterEdit):

    class Meta:
        model = models.Reporte
        fields = ['nombre', 'descripcion', 'tipo', 'cliente', 'lugar', 'estado', 'latitud', 'longitud', 'eliminado']
    # end class
# end class


class FotoReporteForm(forms.ModelForm):

    def clean_foto(self):
        imagen = self.cleaned_data.get('foto', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    class Meta:
        model = models.FotoReporte
        exclude = ()
    # end class
# end class
