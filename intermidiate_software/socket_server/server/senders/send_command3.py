import socket
import json
import random
import zlib
from datetime import datetime

from .server_frames import QUERY_PARAMS_COMMAND


def prepare_data() -> dict:
    '''Creates a message and puts data into it'''

    try:
        message = QUERY_PARAMS_COMMAND                                      # Creating a message
        message['time'] = int(datetime.now().timestamp() * 1_000_000_000)   # Putting a current time (nanosecs)
        message['deviceID'] = random.randint(100_000, 999_999)              # Putting a random device ID

    except Exception as e:
        error = f'PREPARE_DATA ERROR: {e}'
        return {'error': error}
    
    return message


def prepare_message(message: dict) -> tuple[bytes] | dict:
    '''Serializes message to JSON, encodes it, returns packet with messages length, messages content and checksum'''

    try:
        json_message = json.dumps(message)                              # Serializing the message to json
        encoded_message = json_message.encode('utf-8')                  # Encoding message to bytes
    except Exception as e:
        error = f'PREPARE_MESSAGE ERROR (message): {e}'
        return {'error': error}

    try:
        message_length = len(encoded_message)                           # Getting length of the message
        encoded_length = str(message_length).zfill(5).encode('utf-8')   # Encoding length of the message
    except Exception as e:
        error = f'PREPARE_MESSAGE ERROR (length): {e}'
        return {'error': error}

    try:
        checksum = zlib.crc32(encoded_message)                          # Getting checksum of the message
        encoded_checksum = str(checksum).encode('utf-8')                # Encoding checksum
    except Exception as e:
        error = f'PREPARE_MESSAGE ERROR (checksum): {e}'
        return {'error': error}

    return encoded_length, encoded_message, encoded_checksum            # Returning a packet


def send(connection) -> dict:
    '''Sends message with packetType 3 to a client'''

    try:
        message: dict = prepare_data()              # Creating a message
        packet: tuple = prepare_message(message)    # Creating a packet to send (length, message, checksum)

        for data in packet:                         # Running through len-message-checksum list and sending them all
            if isinstance(data, bytes):             # If they are dict, everything was processed properly
                connection.sendall(data)            # Sending them to client
        
        return {'type': 'SENT', 'sentTo': connection.getpeername(), 'message': message} # Returning sent message
    
    except OSError as e:
        error = f'SEND ERROR: {e}'
        return {'error': error}
