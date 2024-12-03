import socket
import time


def init_client(client, address):
    '''Creates a TCPClient object'''

    client.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating a connection

    while True:

        time.sleep(5)                                       # Making a delay
        try:
            client.socket.connect(address)                  # Trying to connect to server
            print("Connection successfully established.")   # Printing a message about establishing of connection
            break                                           # Stopping tries

        except ConnectionRefusedError as e:
            print("ERROR:", e)
            continue

        except TimeoutError as e:
            print("ERROR:", e)
            continue