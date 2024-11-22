import json
import zlib


def match_checksums(message: bytes, checksum: str) -> bool:
    '''Checks if checksum is correct'''

    message_checksum = zlib.crc32(message)

    if message_checksum == int(checksum):
        return True
    return False


def get_packet(server) -> tuple[str] | dict:
    '''Recieves a packet and decodes it, else returns error message'''

    try:
        length: bytes = server.connection.recv(5)
        decoded_length = int(length.decode('utf-8'))

        message: bytes = server.connection.recv(decoded_length)
        checksum: bytes = server.connection.recv(10)

    except Exception as e:
        error = f'GET_PACKET - RECIEVING ERROR: {e}'
        return {'error': error}
    
    try:
        decoded_message = message.decode('utf-8')
        decoded_checksum = checksum.decode('utf-8')

        if not match_checksums(message, decoded_checksum):
            error = 'GET_PACKET - WRONG CHECKSUM ERROR'
            return {'error': error}

    except Exception as e:
        error = f'GET_PACKET - DECODING ERROR: {e}'
        return {'error': error}
    
    return decoded_length, decoded_message, decoded_checksum


def parse_message(packet: tuple[str]) -> str | dict:
    '''Deserialize message to python object and returns it, else returns error message'''

    if isinstance(packet, dict):
        return packet
    
    try:
        message = json.loads(packet[1])

    except Exception as e:
        error = f'PARSE_MESSAGE - JSON PARSING ERROR: {e}'
        return error
    
    return message


def recieve_message(server) -> str | dict:
    '''Executes the recieving message process'''

    packet = get_packet(server)
    message = parse_message(packet)

    return {'type': 'RECIEVED', 'message': message}