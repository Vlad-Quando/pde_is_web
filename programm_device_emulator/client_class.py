from client_source import client_init, recieve_message, handler, closer, send_messages


# Connection data
HOST = "localhost"
# HOST = "213.189.221.17"
PORT = 6000
ADDRESS = (HOST, PORT)


class TCPClient:
    
    def __init__(self):
        return client_init.init_client(self, ADDRESS)

    def recieve(self):
        return recieve_message.recieve_message(self)

    def send(self, packet_type: int):
        return send_messages.send(self, packet_type)

    def handle_connection(self):
        return handler.handle_connection(self)

    def close(self):
        return closer.close(self)