# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from exile.decorator import check_login
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from cuser.middleware import CuserMiddleware
import forms
import models
import json as simplejson
from django.contrib.auth.models import User, Group
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = "http://192.168.1.12:4200"
supra.SupraConf.ACCECC_CONTROL["credentials"] = "true"
supra.SupraConf.ACCECC_CONTROL["headers"] = "origin, content-type, accept"
supra.SupraConf.body = True


class LoginU(supra.SupraSession):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(LoginU, self).dispatch(request, *args, **kwargs)
        return a
    # end def
# end class


class LoginE(supra.SupraSession):
    model = models.Empleado

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(LoginE, self).dispatch(request, *args, **kwargs)
        return a
    # end def
# end class


@supra.access_control
def logoutUser(request):
    logout(request)
    return HttpResponse([], 200)
# end def


@supra.access_control
def islogin(request):
    if request.user.is_authenticated():
        return HttpResponse(simplejson.dumps({"session": request.session.session_key, "username": request.user.username}), 200)
    # end if
    return HttpResponse([], 400)
# end if


class MasterList(supra.SupraListView):

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(MasterList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(MasterList, self).get_queryset()
        if self.request.GET.get('num_page', False):
            self.paginate_by = self.request.GET.get('num_page', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        eliminado = self.request.GET.get('eliminado', False)
        if eliminado == '1':
            queryset = queryset.filter(Q(cuenta__cliente=self.request.user.pk, eliminado=True) | Q(
                cuenta__usuario=self.request.user.pk, eliminado=True))
        else:
            queryset = queryset.filter(Q(cuenta__cliente=self.request.user.pk, eliminado=False) | Q(
                cuenta__usuario=self.request.user.pk, eliminado=False))
            print queryset.count()
        if propiedad and orden:
            if orden == "asc":
                queryset = queryset.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-" + propiedad
                queryset = queryset.order_by(propiedad)
        # end if
        return queryset
    # end def
# end class


"""
    Servicios de Asistente
"""


class AsistenteSupraForm(supra.SupraFormView):
    model = models.Asistente
    form_class = forms.AsistenteForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.AsistenteFormEdit
        # end if
        return self.form_class
    # end class
# end class


class AsistenteSupraFormDelete(supra.SupraDeleteView):
    model = models.Asistente

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class AsistenteList(MasterList):
    model = models.Asistente
    search_key = 'q'
    list_display = ['nombre', 'username', 'identificacion', 'date', 'email', 'direccion',
                    'telefono', 'fijo', 'servicios', 'creator', 'last_editor', 'imagen', 'id', 'cuenta']
    search_fields = ['first_name', 'last_name',
                     'identificacion', 'email', 'username']
    paginate_by = 10

    def nombre(self, obj, row):
        return {'first_name': obj.first_name, 'last_name': obj.last_name}
    # end def

    def date(self, obj, row):
        return obj.fecha_nacimiento.strftime("%Y-%m-%d")
    # end def

    def servicios(self, obj, row):
        edit = "/usuarios/asistente/form/%d/" % (obj.id)
        delete = "/usuarios/asistente/delete/%d/" % (obj.id)
        return {'add': '/usuarios/asistente/form/', 'edit': edit, 'delete': delete}
    # end def
# end class


"""
    Servicios de Cargo
"""


class CargoSupraForm(supra.SupraFormView):
    model = models.Cargo
    form_class = forms.CargoForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CargoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.CargoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class CargoDeleteSupra(supra.SupraDeleteView):
    model = models.Cargo

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CargoDeleteSupra, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class CargoList(MasterList):
    model = models.Cargo
    search_key = 'q'
    list_display = ['nombre', 'date', 'id', 'servicios']
    search_fields = ['nombre', ]
    paginate_by = 10

    def date(self, obj, row):
        return obj.fecha.strftime("%Y-%m-%d")
    # end def

    def servicios(self, obj, row):
        edit = "/usuarios/cargo/form/%d/" % (obj.id)
        delete = "/usuarios/cargo/delete/%d/" % (obj.id)
        return {'add': '/usuarios/cargo/form/', 'edit': edit, 'delete': delete}
    # end def
# end class


"""
    Servicios de empleado
"""


class EmpleadoSupraForm(supra.SupraFormView):
    model = models.Empleado
    form_class = forms.EmpleadoForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.EmpleadoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class EmpleadoSupraFormDelete(supra.SupraDeleteView):
    model = models.Empleado

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class EmpleadoList(MasterList):
    model = models.Empleado
    search_key = 'q'
    list_display = ['nombre', 'username', 'identificacion', 'date', 'email', 'direccion',
                    'telefono', 'fijo', 'servicios', 'creator', 'last_editor', 'ingreso', 'retiro',
                    'imagen', 'id', 'cuenta']
    search_fields = ['first_name', 'last_name',
                     'identificacion', 'email', 'username']
    paginate_by = 10

    def nombre(self, obj, row):
        return {'first_name': obj.first_name, 'last_name': obj.last_name}
    # end def

    def date(self, obj, row):
        return obj.fecha_nacimiento.strftime("%Y-%m-%d")
    # end def

    def ingreso(self, obj, row):
        if obj.fecha_ingreso:
            return obj.fecha_ingreso.strftime("%Y-%m-%d")
        # end if
        return obj.fecha_ingreso
    # end def

    def retiro(self, obj, row):
        if obj.fecha_retiro:
            return obj.fecha_retiro.strftime("%Y-%m-%d")
        # end if
        return obj.fecha_retiro
    # end def

    def servicios(self, obj, row):
        edit = "/usuarios/empleado/form/%d/" % (obj.id)
        delete = "/usuarios/empleado/delete/%d/" % (obj.id)
        return {'add': '/usuarios/empleado/form/', 'edit': edit, 'delete': delete}
    # end def
# end class


"""
    Servicios grupo
"""


class GrupoSupraForm(supra.SupraFormView):
    model = models.Grupo
    form_class = forms.GrupoForm

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(GrupoSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if 'pk' in self.http_kwargs:
            self.form_class = forms.GrupoFormEdit
        # end if
        return self.form_class
    # end class
# end class


class GrupoSupraFormDelete(supra.SupraDeleteView):
    model = models.Grupo

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(GrupoSupraFormDelete, self).dispatch(request, *args, **kwargs)
    # end def

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.eliminado = True
        user = CuserMiddleware.get_user()
        self.object.eliminado_por = user
        self.object.save()
        return HttpResponse(status=200)
    # end def
# end class


class GrupoList(MasterList):
    model = models.Grupo
    search_key = 'q'
    list_display = ['nombre', 'empleados_list']
    search_fields = ['nombre', ]
    paginate_by = 10

    def empleados_list(self, obj, row):
        return dict(models.Empleado.objects.filter(grupo=obj.pk))
    # end def

    def servicios(self, obj, row):
        edit = "/usuarios/grupo/form/%d/" % (obj.id)
        delete = "/usuarios/grupo/delete/%d/" % (obj.id)
        return {'add': '/usuarios/grupo/form/', 'edit': edit, 'delete': delete}
    # end def
# end class
