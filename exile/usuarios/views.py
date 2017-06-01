# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from exile.http import response
from exile.decorator import check_login
from django.http import HttpResponse
from django.db.models import Q
from cuser.middleware import CuserMiddleware
import forms
import models
import json as simplejson
from django.contrib.auth.models import User, Group
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True
supra.SupraConf.ACCECC_CONTROL["origin"] = "http://192.168.1.24:4200"
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


def islogin(request):
    if request.user.is_authenticated():
        return response(simplejson.dumps({"session": request.session.session_key, "username": request.user.username}), 200)
    # end if
    return response([], 400)
# end if


def logoutUsers(request):
    logout(request)
    return response([], 200)
# end def


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


class AsistenteList(supra.SupraListView):
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
    # end defNone

    def servicios(self, obj, row):
        edit = "/usuarios/asistente/form/%d/" % (obj.id)
        delete = "/usuarios/asistente/delete/%d/" % (obj.id)
        return {'add': '/usuarios/asistente/form/', 'edit': edit, 'delete': delete}
    # end def

    @method_decorator(check_login)
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(AsistenteList, self).get_queryset()
        self.paginate_by = self.request.GET.get('num_page', False)
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        queryset = queryset.filter(Q(cuenta__cliente=self.request.user.pk, eliminado=False) | Q(
            cuenta__usuario=self.request.user.pk, eliminado=False))
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
# end class
