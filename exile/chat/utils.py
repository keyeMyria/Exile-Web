from functools import wraps

from .exceptions import ClientError
from .models import Room, Miembro
from subcripcion.models import Cuenta
from django.db.models import Q


def catch_client_error(func):
    """
    Decorator to catch the ClientError exception and translate it into a reply.
    """
    @wraps(func)
    def inner(message, *args, **kwargs):
        try:
            return func(message, *args, **kwargs)
        except ClientError as e:
            # If we catch a client error, tell it to send an error string
            # back to the client on their reply channel
            e.send_to(message.reply_channel)
    return inner

def get_user_or_error(user):
    # Check if the user is logged in
    if not user.is_authenticated():
        raise ClientError("USER_HAS_TO_LOGIN")
    #Busco en mongo al usuario
    miembro = Miembro.objects(usuario=user.pk).first()
    #Si el usuario no existe lo creo
    if not miembro:
        miembro = Miembro(usuario=user.pk, nombre=user.first_name, apellidos=user.last_name, username=user.username)
        cuenta = Cuenta.objects.filter(
            Q(cliente=user.pk) | Q(asistente=user.pk) | Q(empleado=user.pk)).first()
        if cuenta:
            miembro.cuenta = cuenta.id
        # end if
        miembro.save()
    #Si existe altualizo los datos con la informacion diponible en postgrest
    else:
        miembro.update(nombre=user.first_name, apellidos=user.last_name, username=user.username)

    return miembro

def get_room_or_error(room_id, receptores, grupo, user, message):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    miembro = get_user_or_error(user)

    # Find the room they requested (by ID)
    if room_id:
        room = Room.objects(id=room_id)
        if not room:
            raise ClientError("ROOM_INVALID")

    elif receptores:
        miembros = Miembro.objects(usuario__in=receptores)
        list = []
        list.append(miembro)
        for m in miembros:
            list.append(m)

        room = Room(nombre="", grupo=grupo, miembros=list)
        room.save()
        room.websocket_group.add(message.reply_channel)
    else:
        raise ClientError("ROOM_INVALID")
    """
    if room.staff_only and not user.is_staff:
        raise ClientError("ROOM_ACCESS_DENIED")
    """
    return room
