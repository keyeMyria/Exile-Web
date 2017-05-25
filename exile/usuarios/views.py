# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.utils.decorators import method_decorator

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


def logoutUsers(request):
    logout(request)
    return response([], 200)
# end def
