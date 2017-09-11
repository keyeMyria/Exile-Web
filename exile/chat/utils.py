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


def get_room_or_error(room_id, receptores, grupo, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Check if the user is logged in
    if not user.is_authenticated():
        raise ClientError("USER_HAS_TO_LOGIN")
    else:
        usuario = Miembro.objects(usuario=user.pk)
        if not usuario:
            cuenta = models.Cuenta.objects.filter(
                Q(cliente=request.user.pk) | Q(asistente=request.user.pk) | Q(empleado=request.user.pk)).first()
            if cuenta:
                usuario = Miembro(usuario=user.pk, cuenta=cuenta.pk)
                usuario.save()
            else:
                usuario = Miembro(usuario=user.pk)
                usuario.save()

    # Find the room they requested (by ID)
    if room_id:
        room = Room.objects(id=room_id)
        if not room:
            raise ClientError("ROOM_INVALID")

    elif receptores:
        miembros = Miembro.objects(id__in=receptores)
        list = []
        list.append(usuario.id)
        for m in miembros:
            list.append(m.id)
            
        room = Room(nombre="", grupo=grupo, miembros=list)
        room.save()
    else:
        raise ClientError("ROOM_INVALID")
    """
    if room.staff_only and not user.is_staff:
        raise ClientError("ROOM_ACCESS_DENIED")
    """
    return room
