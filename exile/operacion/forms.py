# -*- coding: utf-8 -*-

from django import forms
import models
import widgets


class TareaForm(forms.ModelForm):

    class Meta:
        model = models.Tarea
        exclude = ()
        widgets = {
            #"fecha_de_ejecucion": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y"),
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
