from datetime import datetime
import os
import json

from django.conf import settings

from .server_class import TCPServer


server = None
LOG_FILE = None


def get_log_filename():
    '''Returns name of log-file to create and write'''

    log_dir = os.path.join(settings.BASE_DIR, "logs")               # Getting the logs dir name
    if not os.path.exists(log_dir):                                 # Creating it if its not exist
        os.makedirs(log_dir)

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")     # Getting current date and time
    log_filename = os.path.join(log_dir, current_time + ".json")    # Making a log-filename

    return log_filename


def main():
    '''Creates server object and starts socket server'''

    global server, LOG_FILE

    server = TCPServer()                        # Creating a tcp-server
    LOG_FILE = get_log_filename()               # Getting log filename (not a file yet)
    
    try:
        server.start()                          # Server starts to acquire connections

    except KeyboardInterrupt:
        print("Shutting down the server.")
        server.close()


def process_command2(address: int) -> dict:
    '''Sends command with packetType 2, recieves and prints the answer'''

    global server, LOG_FILE

    connection = False   # Setting current connection to False to use it in if block if there is no client with given address
    
    try:
        if server.connections:                              # If there are clients
            for client in server.connections:               # Running through clients list
                if client[0].getpeername()[1] == address:   # If clients address and the given one matches
                    connection = client[0]                  # Giving the client to the connection variabe
                    break                                   # Stopping loop
        else:
            return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    except Exception as e:
        return {'error': e}
        
    if connection:                                                              # If there is a client
        with open(LOG_FILE, 'a', encoding='utf-8') as log_file:                 # Creating a log file
            sent_message = server.send_command2(connection)                     # Sending command 2
            log_file.write(json.dumps(sent_message, ensure_ascii=False) + '\n') # Writing sent message to buffer
            log_file.flush()                                                    # Writing sent message to log file

            try:
                if sent_message.get('error', None) != None:
                    return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}
            except Exception as e:
                return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}

            commition = server.recieve(connection)                              # Recieving client commition response
            log_file.write(json.dumps(commition, ensure_ascii=False) + '\n')    # Writing recieved message to buffer
            log_file.flush()                                                    # Writing recieved message to log file

            response = server.recieve(connection)                           # Recieving client response
            log_file.write(json.dumps(response, ensure_ascii=False) + '\n') # Writing recieved message to buffer
            log_file.flush()                                                # Writing recieved message to log file

            return {'sent': sent_message, 'commition': commition, 'response': response} # Returning all messages
    
    else:
        return {'error': 'NO CLIENT WITH GIVEN ADDRESS'}

    if server != None:    
        return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    else:
        return {'error': 'ERROR: SERVER HAS NOT STARTED YET'}


def process_command3(address: int) -> dict:
    '''Sends command with packetType 3, recieves and prints the answer'''

    global server, LOG_FILE

    connection = False  # Setting current connection to False to use it in if block if there is no client with given address
    
    try:
        if server.connections:                              # If there are clients
            for client in server.connections:               # Running through clients list
                if client[0].getpeername()[1] == address:   # If clients address and the given one matches
                    connection = client[0]                  # Giving the client to the connection variabe
                    break                                   # Stopping loop
        else:
            return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    except Exception as e:
        return {'error': e}

    if connection:                                                              # If there is a client
        with open(LOG_FILE, 'a', encoding='utf-8') as log_file:                 # Creating a log file
            sent_message = server.send_command3(connection)                     # Sending command 3
            log_file.write(json.dumps(sent_message, ensure_ascii=False) + '\n') # Writing sent message to buffer
            log_file.flush()                                                    # Writing sent message to log file

            try:
                if sent_message.get('error', None) != None:
                    return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}
            except Exception as e:
                return {'error': 'CONNECTION ERROR: CLIENT CLOSED CONNECTION'}

            commition = server.recieve(connection)                              # Recieving client commition response
            log_file.write(json.dumps(commition, ensure_ascii=False) + '\n')    # Writing recieved message to buffer
            log_file.flush()                                                    # Writing recieved message to log file

            response = server.recieve(connection)                               # Recieving client response
            log_file.write(json.dumps(response, ensure_ascii=False) + '\n')     # Writing recieved message to buffer
            log_file.flush()                                                    # Writing recieved message to log file

            return {'sent': sent_message, 'commition': commition, 'response': response} # Returning all messages
    
    else:
        return {'error': 'NO CLIENT WITH GIVEN ADDRESS'}
    
    if server != None:
        return {'error': 'CONNECTION ERROR: NO CLIENTS CONNECTED'}
    else:
        return {'error': 'ERROR: SERVER HAS NOT STARTED YET'}


def process_clients_list() -> tuple | dict:
    '''Returns a list of addresses of clients are in socket servers clients list'''

    global server, LOG_FILE

    try:
        if server.connections:                              # If there are clients
            clients = list()                                # Creating a list with results to return
            for client in server.connections:               # Running through connections list 
                try:
                    commition = server.check_connection(client[0])  # Checking if connection is alive
                    
                    if commition.get('error', False):       # If not
                        server.connections.remove(client)   # Removing client
                        continue                            # Going to next client

                except Exception as e:
                    server.connections.remove(client)       # Removing client if there are problems with connection
                    continue                                # Going to next client

                cur_client = client[0].getpeername()        # Getting current clients address
                clients.append(cur_client)                  # Appending address to result list
                
            if clients:                                     # If there is client (added due to client removing above)
                return {'clients': clients}                 # Returning clients list
            
            return {'clients': 'No clients connected'}
        
        return {'clients': 'No clients connected'}
    except Exception as e:
        return {'error': str(e)}
