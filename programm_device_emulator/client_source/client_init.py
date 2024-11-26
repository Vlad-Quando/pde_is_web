import socket
import time


def init_client(client, address):
    '''Creates a TCPClient object'''

    client.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating a connection

    while True:

        time.sleep(5)
        try:
            client.socket.connect(address)
            print("Connection successfully established.")
            break

        except ConnectionRefusedError as e:
            print("ERROR:", e)
            continue

        except TimeoutError as e:
            print("ERROR:", e)
            continue