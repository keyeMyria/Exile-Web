import models
from http import response
from usuario import models as usuario


def user_plan_operario(view_func):
    def _check(request, *args, **kwargs):
        if request.method in ['POST']:
            if request.user.is_authenticated():
                cuenta = models.Cuenta.objects.filter(cliente__id=request.id).first()
                if cuenta:
                    suscripcion = models.Suscripcion.objects.filter(cuenta=cuenta, activa=True, factura__pagada=True).first()
                    if suscripcion:
                        operario = usuario.Operario.models.filter(cuenta=cuenta, eliminado=False).count()
                        if suscripcion.plan.operadores < operario:
                            return funcion(request, *args, **kwargs)
                        # end if
                        return response(simplejson.dumps({"error": 'Ya registro los %d operarios del plan.'%operario}), 403)
                    #end if
                    return response(simplejson.dumps({"error": "Debe tener una suscripcion activa."}), 403)
                #end if
                return response(simplejson.dumps({"error": "Debe crear una cuenta."}), 403)
            #end if
            return response(simplejson.dumps({"error": "Debes iniciar sesion."}), 403)
        #end if
        return response(simplejson.dumps({"error": "Solicitud incorrecta."}), 403)
    #end def

    return _check
#end def
