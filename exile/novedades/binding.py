import models
from channels.binding.websockets import WebsocketBinding


class TipoReporteValueBinding(WebsocketBinding):
    model = models.TipoReporte
    stream = "tipo_reporte"
    fields = ["nombre", "eliminado"]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class


class ReporteValueBinding(WebsocketBinding):
    model = models.Reporte
    stream = "reporte"
    fields = ["nombre", "descripcion", "tipo", "cliente", "lugar", "fecha", "estado", "latitud", "longitud", "eliminado"]

    @classmethod
    def group_names(cls, instance):
        return ["noti-%d" % instance.cuenta.id]
    # end def

    def has_permission(self, user, action, pk):
        return True
    # end def
# end class
