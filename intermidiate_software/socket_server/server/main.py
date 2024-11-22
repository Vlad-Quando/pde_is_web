from datetime import datetime
import os
import json

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
    
    try:
        server.start() # Starting the server
        LOG_FILE = get_log_filename()

    except KeyboardInterrupt:
        print("Shutting down the server.")
        server.close()


def process_command2(*args, **kwargs) -> dict:
    '''Sends command with packetType 2, recieves and prints the answer'''

    global server, LOG_FILE

    if server.connection:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
            sent_message = server.send_command2()
            log_file.write(json.dumps(sent_message, ensure_ascii=False) + '\n')
            log_file.flush()

            if sent_message.get('error', None) != None:
                return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}

            commition = server.recieve()
            log_file.write(json.dumps(commition, ensure_ascii=False) + '\n')
            log_file.flush()

            response = server.recieve()
            log_file.write(json.dumps(response, ensure_ascii=False) + '\n')
            log_file.flush()

            return {'sent': sent_message, 'commition': commition, 'response': response}

    if server != None:    
        return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    else:
        return {'error': 'ERROR: SERVER HAS NOT STARTED YET'}


def process_command3(*args, **kwargs) -> tuple | str:
    '''Sends command with packetType 3, recieves and prints the answer'''

    global server, LOG_FILE

    if server.connection:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
            sent_message = server.send_command3()
            log_file.write(json.dumps(sent_message, ensure_ascii=False) + '\n')
            log_file.flush()

            if sent_message.get('error', None) != None:
                return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}

            commition = server.recieve()
            log_file.write(json.dumps(commition, ensure_ascii=False) + '\n')
            log_file.flush()

            response = server.recieve()
            log_file.write(json.dumps(response, ensure_ascii=False) + '\n')
            log_file.flush()

            return {'sent': sent_message, 'commition': commition, 'response': response}
    
    if server != None:  
        return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    else:
        return {'error': 'ERROR: SERVER HAS NOT STARTED YET'}
