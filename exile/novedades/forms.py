# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
import models


class TipoReporteForm(forms.ModelForm):

    class Meta:
        model = models.TipoReporte
        exclude = ()
    # end class
# end class


class ReporteSupraForm(forms.ModelForm):

    class Meta:
        model = models.Reporte
        exclude = ()
    # end class
# end class


class FotoReporteForm(forms.ModelForm):

    def clean_url(self):
        imagen = self.cleaned_data.get('url', False)
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
