# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from exile.http import response
import forms
import models
import json as simplejson
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True


class LoginU(supra.SupraSession):
    body = True

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(Login, self).dispatch(request, *args, **kwargs)
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


class AsistenteSupraForm(supra.SupraFormView):
    model = models.Asistente
    form_class = forms.AsistenteForm
    body = True

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AsistenteSupraForm, self).dispatch(request, *args, **kwargs)
    # end def

    def get_form_class(self):
        if self.initial_pk:
            self.form_class = forms.AsistenteFormEdit
        # end if
        return self.form_class
    # end class
# end class
