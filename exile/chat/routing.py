from channels import route
from .consumers import ws_connect, ws_receive, ws_disconnect, send_friends, send_rooms, chat_send, notification_send


# There's no path matching on these routes; we just rely on the matching
# from the top-level routing. We _could_ path match here if we wanted.
websocket_routing = [
    # Called when WebSockets connect
    route("websocket.connect", ws_connect),

    # Called when WebSockets get sent a data frame
    route("websocket.receive", ws_receive),

    # Called when WebSockets disconnect
    route("websocket.disconnect", ws_disconnect),
]


# You can have as many lists here as you like, and choose any name.
# Just refer to the individual names in the include() function.
custom_routing = [
    # Handling different chat commands (websocket.receive is decoded and put
    # onto this channel) - routed on the "command" attribute of the decoded
    # message.
    route("chat.receive", send_friends, command="^friends$"),
    route("chat.receive", send_rooms, command="^rooms$"),
    route("chat.receive", chat_send, command="^send$"),
    route("chat.receive", notification_send, command="^notification$"),
]
