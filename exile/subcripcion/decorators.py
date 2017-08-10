import json as simplejson
from django.shortcuts import redirect, get_object_or_404, HttpResponse
from usuarios import models as usuario
import models
from datetime import datetime
import pytz
from django_user_agents.utils import get_user_agent

def user_plan_operario(view_func):
    def _check(request, *args, **kwargs):
        if (request.method in ['POST'] and kwargs.has_key("pk")) or request.method in ['GET', 'POST', 'PUT'] :
            if request.user.is_authenticated():
                cuenta = models.Cuenta.objects.filter(cliente__id=request.user.id).first()
                if cuenta:
                    suscripcion = models.Suscripcion.objects.filter(cuenta=cuenta, activa=True, factura__paga=True).first()
                    if suscripcion:
                        operario = usuario.Empleado.objects.filter(cuenta=cuenta, eliminado=False).count()
                        print 'esto es lo q hay ',(request.method in ['GET'] and kwargs.has_key("pk")),request.method in ['GET'],kwargs.has_key("pk")

                        if request.method in ['PUT'] or (request.method in ['POST','GET'] and kwargs.has_key("pk") and suscripcion.plan.operadores >= operario) or (request.method in ['GET'] and suscripcion.plan.operadores > operario and not kwargs.has_key("pk")):
                            return view_func(request, *args, **kwargs)
                        # end if
                        return HttpResponse(simplejson.dumps({"error": 'Ya registro los %d operarios del plan.'%operario}), content_type='application/json', status=403)
                    #end if
                    return HttpResponse(simplejson.dumps({"error": "Debe tener una suscripcion activa."}), content_type='application/json', status=403)
                #end if
                return HttpResponse(simplejson.dumps({"error": "Debe crear una cuenta."}), content_type='application/json', status=403)
            #end if
            return HttpResponse(simplejson.dumps({"error": "Debes iniciar session."}), content_type='application/json', status=403)
        #end if
        return HttpResponse(simplejson.dumps({"error": "Solicitud incorrecta."}), content_type='application/json', status=403)
    #end def

    return _check
#end def


def user_plan_asistente(view_func):
    def _check(request, *args, **kwargs):
        if (request.method in ['POST'] and kwargs.has_key("pk")) or request.method in ['GET', 'POST', 'PUT'] :
            if request.user.is_authenticated():
                cuenta = models.Cuenta.objects.filter(cliente__id=request.user.id).first()
                if cuenta:
                    suscripcion = models.Suscripcion.objects.filter(cuenta=cuenta, activa=True, factura__paga=True).first()
                    if suscripcion:
                        operario = usuario.Asistente.objects.filter(cuenta=cuenta, eliminado=False).count()
                        if request.method in ['PUT'] or (request.method in ['POST','GET'] and kwargs.has_key("pk") and suscripcion.plan.operadores >= operario) or (request.method in ['GET'] and suscripcion.plan.operadores > operario and not kwargs.has_key("pk")):
                            return view_func(request, *args, **kwargs)
                        # end if
                        return HttpResponse(simplejson.dumps({"error": 'Ya registro los %d asistentes del plan.'%operario}), content_type='application/json', status=403)
                    #end if
                    return HttpResponse(simplejson.dumps({"error": "Debe tener una suscripcion activa."}), content_type='application/json', status=403)
                #end if
                return HttpResponse(simplejson.dumps({"error": "Debe crear una cuenta."}), content_type='application/json', status=403)
            #end if
            return HttpResponse(simplejson.dumps({"error": "Debes iniciar session."}), content_type='application/json', status=403)
        #end if
        return HttpResponse(simplejson.dumps({"error": "Solicitud incorrecta."}), content_type='application/json', status=403)
    #end def

    return _check
#end def

def user_plan_validar(view_func):
    def _check(request, *args, **kwargs):
        print 'Esta llegando a la validar el plan'
        if request.user.is_authenticated():
            cuenta = models.Cuenta.objects.filter(cliente__id=request.user.id).first()
            if cuenta:
                suscripcion = models.Suscripcion.objects.filter(cuenta=cuenta, activa=True, factura__paga=True).first()
                if suscripcion:
                    if suscripcion.inicio and suscripcion.fin:
                        if datetime.now(pytz.UTC) <= suscripcion.fin:
                            return view_func(request, *args, **kwargs)
                        #end if
                        return HttpResponse(simplejson.dumps({"error": "Su suscripcion esta vencida."}), content_type='application/json', status=403)
                    #end if
                    return HttpResponse(simplejson.dumps({"error": "Debe comunicarse con el administrador del sistema."}), content_type='application/json', status=403)
                #end if
                return HttpResponse(simplejson.dumps({"error": "Debe adquirir un plan de servicio."}), content_type='application/json', status=403)
            #end if
            return HttpResponse(simplejson.dumps({"error": "Debe crear una cuenta."}), content_type='application/json', status=403)
        #end
        return HttpResponse(simplejson.dumps({"error": "Debe iniciar session."}), content_type='application/json', status=403)
    #end def

    return _check
#end def


def user_plan_validar_app_operario(view_func):
    def _check(request, *args, **kwargs):
        print 'Esta llegando a la validar el plan'
        if request.user.is_authenticated():
            cuenta = models.Cuenta.objects.filter(cliente__id=request.user.id).first()
            if cuenta:
                suscripcion = models.Suscripcion.objects.filter(cuenta=cuenta, activa=True, factura__paga=True).first()
                if suscripcion:
                    empleado = usuario.Empleado.objects.filter(cuenta=cuenta,id=request.id).first()
                    if empleado:
                        if suscripcion.plan.operario:
                            return view_func(request, *args, **kwargs)
                        #end if
                        return HttpResponse(simplejson.dumps({"error": "Su plan no cuenta con acceso al app."}), content_type='application/json', status=403)
                    #end if
                    return HttpResponse(simplejson.dumps({"error": "No cuenta con los permisos necesarios."}), content_type='application/json', status=403)
                #end if
                return HttpResponse(simplejson.dumps({"error": "Debe adquirir un plan de servicio."}), content_type='application/json', status=403)
            #end if
            return HttpResponse(simplejson.dumps({"error": "Debe crear una cuenta."}), content_type='application/json', status=403)
        #end
        return HttpResponse(simplejson.dumps({"error": "Debe iniciar session."}), content_type='application/json', status=403)
    #end def

    return _check
#end def
