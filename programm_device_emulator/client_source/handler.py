def handle_connection(client):
    '''Processes the connection with the server'''

    while True:
        try:
            message = client.recieve()              # Recieving message from server
            packet_type = message.get('packetType', None)     # Getting its packetType
            print('RECIEVED', message)              # Printing recieved message

            message = client.send(18)               # Sending a commition to server
            print('SENT', message)                  # Printing sent commition

            if packet_type == 3:                    # Sending appropriate responses to server depending on packetType
                message = client.send(1)
            elif packet_type == 2:
                message = client.send(4)
            elif packet_type == 104:
                message = client.send(105)
            else:
                print("HANDLE_CONNECTION ERROR - packetType is None")
                break
            
            print('SENT', message)                  # Printing sent message
            print()
        
        except Exception as e:
            print("ERROR", e)
            # print('HANDLE_CONNECTION ERROR', e)
            break