import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer
import binding


"""
    Binding
"""


class OperacionDemultiplexerBiding(WebsocketDemultiplexer):

    consumers = {
        "tipo": binding.TipoValueBinding.consumer,
        "cliente": binding.ClienteValueBinding.consumer,
        "lugar": binding.LugarValueBinding.consumer,
        "tarea": binding.TareaValueBinding.consumer,
        "subtarea": binding.SubTareaValueBinding.consumer,
        "completado": binding.SubTareaValueBinding.consumer,
        "multimedia": binding.MultimediaValueBinding.consumer,
        "completadosub": binding.CompletadoSubValueBinding.consumer
    }

    def connection_groups(self, **kwargs):
        return ["noti-%s" % kwargs["pk"]]
    # end def
# end class
