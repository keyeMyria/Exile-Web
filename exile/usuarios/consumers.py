import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from subcripcion.models import Cuenta
from django.db.models import Q


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    if message.user:
        cuenta = Cuenta.objects.filter(Q(cliente=message.user.pk) | Q(usuario=message.user.pk)).first()
        if cuenta:
            Group('noti-%d' % cuenta.id).add(message.reply_channel)
            Group('noti-%d' % cuenta.id).send({
                'text': json.dumps({
                    'username': message.user.username,
                    'is_logged_in': True
                })
            })


@channel_session_user
def ws_disconnect(message):
    if message.user:
        cuenta = Cuenta.objects.filter(Q(cliente=message.user.pk) | Q(usuario=message.user.pk)).first()
        if cuenta:
            Group('noti-%d' % cuenta.id).send({
                'text': json.dumps({
                    'username': message.user.username,
                    'is_logged_in': False
                })
            })
            Group('noti-%d' % cuenta.id).discard(message.reply_channel)
