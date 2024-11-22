def start(server):
    '''Starts the loop of awaiting of clients'''
    
    # Server loop
    while True:

        connection, address = server.socket.accept() # Establishing a connection
        server.connection = connection
        server.address = address
        print("Connected to", address)

        break


def close(server):
    '''Shuts down the server and closes all connections'''

    if server.connection != None:
        server.connection.close()
        print("Server closed.")
    else:
        print('CLOSE ERROR: No clients connected')
