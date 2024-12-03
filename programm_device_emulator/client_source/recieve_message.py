import json
import zlib


def match_checksums(message: bytes, checksum: str) -> bool:
    '''Checks if checksum is correct'''

    message_checksum = zlib.crc32(message)      # Calculating checksum of recieved message

    if message_checksum == int(checksum):       # Matching calculated and given checksums
        return True
    return False


def get_packet(connection) -> tuple[str] | dict:
    '''Recieves a packet and decodes it, else returns error message'''

    try:
        length: bytes = connection.recv(5)                  # Recieving message length
        decoded_length = int(length.decode('utf-8'))        # Decoding message length and casting it to int
        
    except Exception as e:
        error = f'GET_PACKET - RECIEVING or DECODING LENGTH ERROR: {e}'
        return {'error': error}

    try:
        message: bytes = connection.recv(decoded_length)    # Recieving message of given length
    except Exception as e:
        error = f'GET_PACKET - RECIEVING MESSAGE ERROR: {e}'
        return {'error': error}

    try:
        checksum: bytes = connection.recv(10)               # Recieving checksum

    except Exception as e:
        error = f'GET_PACKET - RECIEVING CHECKSUM ERROR: {e}'
        return {'error': error}
    
    try:
        decoded_message = message.decode('utf-8')           # Decoding message
        decoded_checksum = checksum.decode('utf-8')         # Decoding checksum

        if not match_checksums(message, decoded_checksum):  # Checking checksum
            error = 'GET_PACKET - WRONG CHECKSUM ERROR'
            return {'error': error}

    except Exception as e:
        error = f'GET_PACKET - DECODING MESSAGE of CHECKSUM ERROR: {e}'
        return {'error': error}
    
    return decoded_length, decoded_message, decoded_checksum # Returning message length, message and checksum


def parse_message(packet: tuple[str]) -> str | dict:
    '''Deserialize message to python object and returns it, else returns error message'''

    if isinstance(packet, dict):            # If it is dict, an error occured
        return packet
    
    try:
        message = json.loads(packet[1])     # Deserializing message

    except Exception as e:
        error = f'PARSE_MESSAGE - JSON PARSING ERROR: {e}'
        return {'error': error}
    
    return message


def recieve_message(client) -> str | dict:
    '''Executes the recieving message process'''

    packet = get_packet(client)         # Recieving packet
    message = parse_message(packet)     # Deserializing message

    return message                      # Returning recieved message