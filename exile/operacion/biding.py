import models
from channels.binding.websockets import WebsocketBinding


class ClienteValueBinding(WebsocketBinding):
    model = models.Cliente
    stream = "cliente"
    fields = ["nombre", '']
