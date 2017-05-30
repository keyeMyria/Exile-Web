# -*- coding: utf-8 -*-
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


class ClienteForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
    # end def

    def clean(self):
        data = super(ClienteForm, self).clean()
        if data.get('identificacion'):
            if models.Cliente.objects.filter(identificacion=data.get('identificacion')).first():
                self.add_error('first_name','El cliente se encuentra registrado')
            #end def
    #end def

    class Meta:
        model = models.Cliente
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name','identificacion',
         'direccion','telefono']
        exclude = ['estado']
    # end class

    def save(self, commit = True):
        cliente = super(ClienteForm, self).save(commit=False)
        cliente.save()
        cuenta = models.Cuenta(cliente=cliente,estado=True)
        cuenta.save()
        return cliente
    #end def
#end class


class ClienteEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
    # end def

    class Meta:
        model = models.Cliente
        fields = ['username', 'email', 'first_name','last_name', 'identificacion',
         'direccion', 'telefono']
        exclude = ['estado', 'password1', 'password2']
    # end class
#end class
