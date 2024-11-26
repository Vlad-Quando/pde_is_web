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

    def send_command2(self, connection):
        return send_command2.send(connection)

    def send_command3(self, connection):
        return send_command3.send(connection)

    def recieve(self, connection):
        return recieve_message.recieve_message(connection)

    def start(self):
        return start_close.start(self)

    def close(self):
        return start_close.close(self)
