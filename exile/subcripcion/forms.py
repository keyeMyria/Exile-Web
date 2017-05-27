from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
import models


class ModuloForm(forms.ModelForm):
    class Meta:
        model = models.Modulo
        fields = ['nombre','descripcion','estado']
        exclude = []
    #end class

    def save(self, commit=True):
        modulo = super(ModuloForm, self).save(commit)
        modulo.nombre = modulo.nombre.title()
        modulo.save()
        return modulo
    # end def
#end class


class FuncionalidadForm(forms.ModelForm):
    class Meta:
        model = models.Funcionalidad
        fields = ['modulo','nombre','url', 'descripcion', 'estado']
        exclude = []
    #end class

    def save(self, commit=True):
        modulo = super(FuncionalidadForm, self).save(commit)
        modulo.nombre = modulo.nombre.title()
        modulo.save()
        return modulo
    # end def
#end class


class FuncionalidadForm(forms.ModelForm):
    class Meta:
        model = models.Funcionalidad
        fields = ['modulo','nombre','url', 'descripcion', 'estado']
        exclude = []
    #end class

    def save(self, commit=True):
        modulo = super(FuncionalidadForm, self).save(commit)
        modulo.nombre = modulo.nombre.title()
        modulo.save()
        return modulo
    # end def
#end class


class InstModuloForm(forms.ModelForm):
    class Meta:
        model = models.InstModulo
        fields = ['nombre', 'descripcion', 'modulo', 'funcionalidades', 'estado']
        exclude = []
    #end class

    def save(self, commit=True):
        modulo = super(InstModuloForm, self).save(commit)
        modulo.nombre = modulo.nombre.title()
        modulo.save()
        return modulo
    # end def
#end class


class PlanForm(forms.ModelForm):
    class Meta:
        model = models.Plan
        fields = ['nombre', 'operadores', 'asistentes', 'descripcion', 'valor', 'duracion', 'modulos' ,'estado']
        exclude = []
    #end class

    def save(self, commit=True):
        modulo = super(PlanForm, self).save(commit)
        modulo.nombre = modulo.nombre.title()
        modulo.save()
        return modulo
    # end def
#end class
