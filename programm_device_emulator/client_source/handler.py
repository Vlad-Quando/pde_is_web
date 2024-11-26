def handle_connection(client):
    '''Processes the connection with the server'''

    while True:
        try:
            message = client.recieve()
            packet_type = message['packetType']
            print('RECIEVED', message)

            message = client.send(18)
            print('SENT', message)

            if packet_type == 3:
                message = client.send(1)
            elif packet_type == 2:
                message = client.send(4)
            
            print('SENT', message)
            print()
        
        except Exception as e:
            print('HANDLE_CONNECTION ERROR', e)
            break