import threading

from django.apps import AppConfig
from .server import main


tcp_server = None


class SocketServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'socket_server'

    def ready(self):

        global tcp_server

        tcp_server = threading.Thread(target=main.main)     # Creating a socket-server thread
        tcp_server.setDaemon(True)                          # Making it daemonic
        tcp_server.start()                                  # Starting the socket-server thread

        return super().ready()
