from datetime import datetime
import os
import json
from threading import Thread

from django.conf import settings

from .server_class import TCPServer


server = None
LOG_FILE = None


def get_log_filename():
    '''Returns name of log-file to create and write'''

    log_dir = os.path.join(settings.BASE_DIR, "logs") # Getting the logs dir name
    if not os.path.exists(log_dir): # Creating it if its not exist
        os.makedirs(log_dir)

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Getting current date and time
    log_filename = os.path.join(log_dir, current_time + ".json") # Making a log-filename

    return log_filename


def main():
    global server, LOG_FILE

    server = TCPServer() # Creating a tcp-server
    LOG_FILE = get_log_filename()
    
    try:
        server.start() # Starting the server

    except KeyboardInterrupt:
        print("Shutting down the server.")
        server.close()
        # del server


def process_command2(address: int) -> dict:
    '''Sends command with packetType 2, recieves and prints the answer'''

    global server, LOG_FILE

    connection = False
    
    try:
        if len(server.connections) > 0:
            for client in server.connections:
                if client[0].getpeername()[1] == address:
                    connection = client[0]
                    break
        else:
            return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    except Exception as e:
        return {'error': e}
        
    if connection:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
            sent_message = server.send_command2(connection)
            log_file.write(json.dumps(sent_message, ensure_ascii=False) + '\n')
            log_file.flush()

            try:
                if sent_message.get('error', None) != None:
                    return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}
            except Exception as e:
                return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}

            commition = server.recieve(connection)
            log_file.write(json.dumps(commition, ensure_ascii=False) + '\n')
            log_file.flush()

            response = server.recieve(connection)
            log_file.write(json.dumps(response, ensure_ascii=False) + '\n')
            log_file.flush()

            return {'sent': sent_message, 'commition': commition, 'response': response}
    
    else:
        return {'error': 'NO CLIENT WITH GIVEN ADDRESS'}

    if server != None:    
        return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    else:
        return {'error': 'ERROR: SERVER HAS NOT STARTED YET'}


def process_command3(address: int) -> dict:
    '''Sends command with packetType 3, recieves and prints the answer'''

    global server, LOG_FILE

    connection = False
    
    try:
        if len(server.connections) > 0:
            for client in server.connections:
                if client[0].getpeername()[1] == address:
                    connection = client[0]
                    break
        else:
            return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    except Exception as e:
        return {'error': e}

    if connection:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
            sent_message = server.send_command3(connection)
            log_file.write(json.dumps(sent_message, ensure_ascii=False) + '\n')
            log_file.flush()

            try:
                if sent_message.get('error', None) != None:
                    return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}
            except Exception as e:
                return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}

            commition = server.recieve(connection)
            log_file.write(json.dumps(commition, ensure_ascii=False) + '\n')
            log_file.flush()

            response = server.recieve(connection)
            log_file.write(json.dumps(response, ensure_ascii=False) + '\n')
            log_file.flush()

            return {'sent': sent_message, 'commition': commition, 'response': response}
    
    else:
        return {'error': 'NO CLIENT WITH GIVEN ADDRESS'}
    
    if server != None:  
        return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    else:
        return {'error': 'ERROR: SERVER HAS NOT STARTED YET'}


def process_clients_list(*args, **kwargs) -> tuple | dict:

    global server, LOG_FILE

    try:
        if server.connections:
            clients = list()
            for client in server.connections:
                try:
                    cur_client = client[0].getpeername()
                    clients.append(cur_client)
                except Exception as e:
                    server.connections.remove(client)
            if clients:
                return {'clients': clients}
            return {'clients': 'No clients connected'}
        
        return {'clients': 'No clients connected'}
    except Exception as e:
        return {'error': str(e)}
