import json
from channels import Channel, Group
from channels.auth import channel_session_user_from_http, channel_session_user
from django.db.models import Q
from .settings import MSG_TYPE_LEAVE, MSG_TYPE_ENTER, NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS
from .models import Room, Miembro, NotificationRoom, Notification
from .utils import get_room_or_error, catch_client_error, get_user_or_error
from .exceptions import ClientError
from subcripcion.models import Cuenta
from .models import Miembro


### WebSocket handling ###


# This decorator copies the user from the HTTP session (only available in
# websocket.connect or http.request messages) to the channel session (available
# in all consumers with the same reply_channel, so all three here)

@channel_session_user_from_http
def ws_connect(message):
    context = {'accept': message.user.is_authenticated()}
    message.reply_channel.send(context)
    # Initialise their session
    message.channel_session['rooms'] = []
    # Verificao si el usuario existe en la base de datos mongo
    miembro = get_user_or_error(message.user)
    Group('miembro-%s' % miembro.usuario).add(message.reply_channel)

# Unpacks the JSON in the received WebSocket frame and puts it onto a channel
# of its own with a few attributes extra so we can route it
# This doesn't need @channel_session_user as the next consumer will have that,
# and we preserve message.reply_channel (which that's based on)
def ws_receive(message):
    # All WebSocket frames have either a text or binary payload; we decode the
    # text part here assuming it's JSON.
    # You could easily build up a basic framework that did this encoding/decoding
    # for you as well as handling common errors.
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.receive").send(payload)


@channel_session_user
def ws_disconnect(message):
    # Unsubscribe from any connected rooms
    if message.user.is_authenticated():
        Group('miembro-%s' % message.user.pk).discard(message.reply_channel)
    for room_id in message.channel_session.get("rooms", set()):
        room = Room.objects(id=room_id).first()
            # Removes us from the room's send group. If this doesn't get run,
            # we'll get removed once our first reply message expires.
        if room:
            room.websocket_group.discard(message.reply_channel)



### Chat channel handling ###
@channel_session_user
@catch_client_error
def send_friends(message):
    # Busco al usuario en la base de datos mongo
    miembro = get_user_or_error(message.user)
    #Busco a todas las personas relacionadas a la cuenta del usuario que se acaba de conectar

    miembros = Miembro.objects(cuenta=miembro.cuenta)
    lista = []
    for m in miembros:
        data = {"id": str(m.id), "username": m.username, "nombre": m.nombre, "apellidos": m.apellidos, "usuario_id": m.usuario, "cuenta_id": m.cuenta }
        lista.append(data)

    #Creo un agrego un grupo para la persona que se acaba de conectar, para poder enviarle la lista de usuarios
    # y las salas y los mensajes
    Group('miembro-%s' % miembro.usuario).send({
        'text': json.dumps({
            'friends': lista,
            'type': 'friends'
        })
    })


@channel_session_user
@catch_client_error
def send_rooms(message):
    # Verificao si el usuario existe en la base de datos mongo
    miembro = get_user_or_error(message.user)
    rooms = Room.objects(miembros__in=[miembro])
    lista = []
    for r in rooms:
        r.websocket_group.add(message.reply_channel)
        message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([str(r.id)]))
        lista.append({"id": str(r.id), "grupo": r.grupo, "nombre": r.nombre, "miembros": r.list_miembros, "me": str(miembro.id) })
    # data = json.loads(rooms.to_json())
    Group('miembro-%s' % miembro.usuario).send({
        'text': json.dumps({
            'rooms': lista,
            'type': 'rooms'
        })
    })


@channel_session_user
@catch_client_error
def chat_send(message):
    # Find the room they're sending to, check perms
    room = get_room_or_error(message["room"], message["miembros"], message["grupo"], message.user, message)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([str(room.id)]))
    # Send the message along
    miembro = get_user_or_error(message.user)
    room.send_message(message["message"], miembro)


@channel_session_user
@catch_client_error
def notification_send(message):
    miembro = get_user_or_error(message.user)
    notification_room = NotificationRoom.objects(miembro=miembro)
    notification = Notification.objects(miembro=miembro)
    Group('miembro-%s' % miembro.usuario).send({
        'text': json.dumps({
            "type": "notification",
            "notifications": json.loads(notification.to_json()),
            "notifications_room": json.loads(notification_room.to_json())
        })
    })


"""
 Falta por hacer los siguientes consumidores:
 * notificacion recibida
 * notificacion romm recibida
 * mensaje recibido
 * mensaje visto
"""
