import json as simplejson
from django.shortcuts import redirect, get_object_or_404, HttpResponse
from usuarios import models as usuario
import models


def user_plan_operario(view_func):
    def _check(request, *args, **kwargs):
        if (request.method in ['POST'] and kwargs['pk']) or request.method in ['GET', 'POST', 'PUT'] :
            if request.user.is_authenticated():
                cuenta = models.Cuenta.objects.filter(cliente__id=request.user.id).first()
                if cuenta:
                    suscripcion = models.Suscripcion.objects.filter(cuenta=cuenta, activa=True, factura__paga=True).first()
                    if suscripcion:
                        operario = usuario.Empleado.objects.filter(cuenta=cuenta, eliminado=False).count()
                        if request.method in ['PUT'] or (request.method in ['POST'] and kwargs['pk']) or (request.method in ['GET'] and suscripcion.plan.operadores > operario) or (suscripcion.plan.operadores >= operario+1 and request.method in ['POST'] and not kwargs['pk']):
                            return view_func(request, *args, **kwargs)
                        # end if
                        return HttpResponse(simplejson.dumps({"error": 'Ya registro los %d operarios del plan.'%operario}), content_type='application/json', status=403)
                    #end if
                    return HttpResponse(simplejson.dumps({"error": "Debe tener una suscripcion activa."}), content_type='application/json', status=403)
                #end if
                return HttpResponse(simplejson.dumps({"error": "Debe crear una cuenta."}), content_type='application/json', status=403)
            #end if
            return HttpResponse(simplejson.dumps({"error": "Debes iniciar sesion."}), content_type='application/json', status=403)
        #end if
        return HttpResponse(simplejson.dumps({"error": "Solicitud incorrecta."}), content_type='application/json', status=403)
    #end def

    return _check
#end def


def user_plan_asistente(view_func):
    def _check(request, *args, **kwargs):
        if (request.method in ['POST'] and kwargs['pk']) or request.method in ['GET', 'POST', 'PUT'] :
            if request.user.is_authenticated():
                cuenta = models.Cuenta.objects.filter(cliente__id=request.user.id).first()
                if cuenta:
                    suscripcion = models.Suscripcion.objects.filter(cuenta=cuenta, activa=True, factura__paga=True).first()
                    if suscripcion:
                        operario = usuario.Asistente.objects.filter(cuenta=cuenta, eliminado=False).count()
                        if request.method in ['PUT'] or (request.method in ['POST'] and kwargs['pk']) or (request.method in ['GET'] and suscripcion.plan.operadores > operario) or (suscripcion.plan.operadores >= operario+1 and request.method in ['POST'] and not kwargs['pk']):
                            return view_func(request, *args, **kwargs)
                        # end if
                        return HttpResponse(simplejson.dumps({"error": 'Ya registro los %d asistentes del plan.'%operario}), content_type='application/json', status=403)
                    #end if
                    return HttpResponse(simplejson.dumps({"error": "Debe tener una suscripcion activa."}), content_type='application/json', status=403)
                #end if
                return HttpResponse(simplejson.dumps({"error": "Debe crear una cuenta."}), content_type='application/json', status=403)
            #end if
            return HttpResponse(simplejson.dumps({"error": "Debes iniciar sesion."}), content_type='application/json', status=403)
        #end if
        return HttpResponse(simplejson.dumps({"error": "Solicitud incorrecta."}), content_type='application/json', status=403)
    #end def

    return _check
#end def
