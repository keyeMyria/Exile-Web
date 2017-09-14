import json
from channels import Channel, Group
from channels.auth import channel_session_user_from_http, channel_session_user
from django.db.models import Q
from .settings import MSG_TYPE_LEAVE, MSG_TYPE_ENTER, NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS
from .models import Room, Miembro
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
    message.reply_channel.send({'accept': True})
    # Initialise their session
    message.channel_session['rooms'] = []
    miembro = get_user_or_error(message.user)
    # Verificao si el usuario existe en la base de datos mongo
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
        try:
            room = Room.objects(id=room_id)
            # Removes us from the room's send group. If this doesn't get run,
            # we'll get removed once our first reply message expires.
            room.websocket_group.discard(message.reply_channel)
        except Room.DoesNotExist:
            pass


### Chat channel handling ###
@channel_session_user
@catch_client_error
def send_friends(message):
    # Busco al usuario en la base de datos mongo
    miembro = get_user_or_error(message.user)

    #Busco a todas las personas relacionadas a la cuenta del usuario que se acaba de conectar
    listaM = Miembro.objects(cuenta=miembro.cuenta).to_json()
    data = json.loads(listaM)
    #Creo un agrego un grupo para la persona que se acaba de conectar, para poder enviarle la lista de usuarios
    # y las salas y los mensajes
    Group('miembro-%s' % miembro.usuario).send({
        'text': json.dumps({
            'friends': data
        })
    })


@channel_session_user
@catch_client_error
def send_rooms(message):
    user = message.user
    # Verificao si el usuario existe en la base de datos mongo
    miembro = get_user_or_error(message.user)
    print miembro
    rooms = Room.objects(miembros__in=[miembro])
    for r in rooms:
        r.websocket_group.add(message.reply_channel)
        message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([r.id]))

    data = json.loads(rooms.to_json())
    Group('miembro-%s' % miembro.usuario).send({
        'text': json.dumps({
            'rooms': data
        })
    })

# Channel_session_user loads the user out from the channel session and presents
# it as message.user. There's also a http_session_user if you want to do this on
# a low-level HTTP handler, or just channel_session if all you want is the
# message.channel_session object without the auth fetching overhead.
@channel_session_user
@catch_client_error
def chat_join(message):
    # Find the room they requested (by ID) and add ourselves to the send group
    # Note that, because of channel_session_user, we have a message.user
    # object that works just like request.user would. Security!
    room = get_room_or_error(message["room"], mensaje["receptores"], mensaje["grupo"], message.user)

    # Send a "enter message" to the room if available
    if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
        room.send_message(None, message.user, MSG_TYPE_ENTER)

    # OK, add them in. The websocket_group is what we'll send messages
    # to so that everyone in the chat room gets them.
    room.websocket_group.add(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
    # Send a message back that will prompt them to open the room
    # Done server-side so that we could, for example, make people
    # join rooms automatically.
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(room.id),
            "title": room.title,
        }),
    })


@channel_session_user
@catch_client_error
def chat_leave(message):
    # Reverse of join - remove them from everything.
    room = get_room_or_error(message["room"], False, False, message.user)

    # Send a "leave message" to the room if available
    if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
        room.send_message(None, message.user, MSG_TYPE_LEAVE)

    room.websocket_group.discard(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).difference([room.id]))
    # Send a message back that will prompt them to close the room
    message.reply_channel.send({
        "text": json.dumps({
            "leave": str(room.id),
        }),
    })


@channel_session_user
@catch_client_error
def chat_send(message):
    # Check that the user in the room
    if int(message['room']) not in message.channel_session['rooms']:
        raise ClientError("ROOM_ACCESS_DENIED")
    # Find the room they're sending to, check perms
    room = get_room_or_error(message["room"], mensaje["miembros"], mensaje["grupo"], message.user, message)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([r.id]))
    # Send the message along
    room.send_message(message["message"], message.user)
