import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from subcripcion.models import Cuenta
from django.db.models import Q
from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer, WebsocketConsumer
import binding



@channel_session_user_from_http
def ws_connect(message, pk):
    message.reply_channel.send({"accept": True})
    Group('noti-%s' % pk).add(message.reply_channel)
    Group('noti-%s' % pk).send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })


@channel_session_user
def ws_disconnect(message, pk):
    Group('noti-%s' % pk).send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('noti-%s' % pk).discard(message.reply_channel)


def ws_receive(messag, pk):
    Group('noti-%s' % pk).send({
        'text': json.dumps({
            'username': message.user.username,
            'message': message.content
        })
    })


"""
    Binding
"""


class UsuariosDemultiplexerBiding(WebsocketDemultiplexer):

    consumers = {
        "cargo": binding.CargoValueBinding.consumer,
        "empleado": binding.EmpleadoValueBinding.consumer,
        "asistente": binding.AsistenteValueBinding.consumer,
        "grupo": binding.GrupoValueBinding.consumer
    }

    def connection_groups(self, **kwargs):
        return ["noti-%s" % kwargs["pk"]]
    # end def
# end class
