import models
from channels.binding.websockets import WebsocketBinding


class TipoValueBinding(WebsocketBinding):
    model = models.Tipo
    stream = "tipo"
    fields = ["nombre", "eliminado"]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class ClienteValueBinding(WebsocketBinding):
    model = models.Cliente
    stream = "cliente"
    fields = ["nombre", 'tipo', "tipo__nombre", 'identificacion', 'direccion', 'telefono', 'eliminado']

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class LugarValueBinding(WebsocketBinding):
    model = models.Lugar
    stream = "lugar"
    fields = ["nombre", 'direccion', "latitud", 'longitud', 'eliminado']

    @classmethod
    def group_names(cls, instance):
        print "entro a lugar"
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class TareaValueBinding(WebsocketBinding):
    model = models.Tarea
    stream = "tarea"
    fields = ["nombre", 'descripcion', "fecha_de_ejecucion", 'lugar', 'cliente', 'empleados', 'grupo', 'sub_complete']

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class SubTareaValueBinding(WebsocketBinding):
    model = models.SubTarea
    stream = "subtarea"
    fields = ["tarea", "nombre", "descripcion", "eliminado"]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.tarea.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class CompletadoValueBinding(WebsocketBinding):
    model = models.Completado
    stream = "completado"
    fields = ["tarea", "fecha", "terminado", "creator"]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.tarea.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class MultimediaValueBinding(WebsocketBinding):
    model = models.Multimedia
    stream = "multimedia"
    fields = ["completado", "archivo", "audio", "foto"]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.completado.tarea.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class CompletadoSubValueBinding(WebsocketBinding):
    model = models.CompletadoSub
    stream = "completadosub"
    fields = ["subtarea", "creator", "fecha"]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.subtarea.tarea.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class
