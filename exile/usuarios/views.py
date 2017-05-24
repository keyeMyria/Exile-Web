# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.utils.decorators import method_decorator

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True


class Login(supra.SupraSession):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)
    # end def
# end class
