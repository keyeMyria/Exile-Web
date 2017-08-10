import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer
import binding


"""
    Binding
"""


class NovedadesDemultiplexerBiding(WebsocketDemultiplexer):

    consumers = {
        "tipo_reporte": binding.TipoReporteValueBinding.consumer,
        "reporte": binding.ReporteValueBinding.consumer
    }

    def connection_groups(self, **kwargs):
        return ["noti-%s" % kwargs["pk"]]
    # end def
# end class
