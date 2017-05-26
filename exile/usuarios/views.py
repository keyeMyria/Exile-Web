# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from exile.http import response
import json as simplejson
# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True


class Login(supra.SupraSession):
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
