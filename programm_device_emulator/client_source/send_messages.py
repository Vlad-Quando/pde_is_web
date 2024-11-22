import random
import json
import zlib
from datetime import datetime

from .client_frames import *


def prepare_commition() -> dict:
    '''Creates a commition message and puts data into it'''

    try:
        message = DATA_RECEPTION_COMMITION # Creating a message
        message['time'] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)
        message['deviceID'] = random.randint(100_000, 999_999) # Putting a random device ID
        
    except Exception as e:
        error = f'PREPARE_COMMITION ERROR: {e}'
        return {'error': error}
    
    return message


def prepare_params_data() -> dict:
    '''Creates a params data message and puts data into it'''
    
    try:
        message = PARAMS_DATA_COMMAND # Creating a message
        message['time'] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)
        message['deviceID'] = random.randint(100_000, 999_999) # Putting a random device ID
        
    except Exception as e:
        error = f'PREPARE_PARAMS_DATA ERROR: {e}'
        return {'error': error}
    
    return message


def prepare_detection_data() -> dict:
    '''Creates a detection data message and puts data into it'''

    try:
        message = DETECTION_DATA_FRAME # Creating a message
        message['time'] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)
        message['deviceID'] = random.randint(100_000, 999_999) # Putting a random device ID
        
    except Exception as e:
        error = f'PREPARE_DETECTION_DATA ERROR: {e}'
        return {'error': error}
    
    return message


def prepare_message(message: dict) -> tuple[bytes] | dict:
    '''Serializes message to JSON, encodes it, returns packet with messages length, messages content and checksum'''

    try:
        json_message = json.dumps(message) # Serializing the message to json
        encoded_message = json_message.encode('utf-8') # Encoding message to bytes
    except Exception as e:
        error = f'PREPARE_MESSAGE ERROR (message): {e}'
        return {'error': error}

    try:
        message_length = len(encoded_message) # Getting length of the message
        encoded_length = str(message_length).zfill(5).encode('utf-8') # Encoding length of the message
    except Exception as e:
        error = f'PREPARE_MESSAGE ERROR (length): {e}'
        return {'error': error}

    try:
        checksum = zlib.crc32(encoded_message) # Getting checksum of the message
        encoded_checksum = str(checksum).encode('utf-8') # Encoding checksum
    except Exception as e:
        error = f'PREPARE_MESSAGE ERROR (checksum): {e}'
        return {'error': error}

    return encoded_length, encoded_message, encoded_checksum


def send(client, packet_type) -> str | dict:
    '''Sends message with packetType 3 to a client'''

    try:
        if packet_type == 18:
            message: dict = prepare_commition()
        elif packet_type == 1:
            message: dict = prepare_detection_data()
        elif packet_type == 4:
            message: dict = prepare_params_data()

        packet: tuple = prepare_message(message)

        for data in packet:
            if isinstance(data, bytes):
                client.socket.sendall(data)
        
        return {'type': 'SENT', 'message': message}
    
    except OSError as e:
        error = f'SEND ERROR: {e}'
        return {'error': error}