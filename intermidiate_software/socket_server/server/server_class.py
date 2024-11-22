import socket

from . import server_init
from . import start_close
from .senders import send_command2, send_command3
from .recievers import recieve_message


# Connection data
HOST = "localhost"
# HOST = "213.189.221.17"
PORT = 6000
ADDRESS = (HOST, PORT)


class TCPServer:

    def __init__(self):
        return server_init.init_server(self, ADDRESS, HOST, PORT)

    def send_command2(self):
        return send_command2.send(self)

    def send_command3(self):
        return send_command3.send(self)

    def recieve(self):
        return recieve_message.recieve_message(self)

    def start(self):
        return start_close.start(self)

    def close(self):
        return start_close.close(self)
