import select


def start(server):
    '''Starts the loop of awaiting of clients'''
    
    # Server loop
    while True:
        try:
            connection, address = server.socket.accept() # Establishing a connection
            server.connections.append((connection, address))
            print("Connected to", address, connection)
        except Exception as e:
            print("Error while starting accepting clients loop:", e)
            break


def close(server):
    '''Shuts down the server and closes all connections'''

    if server.connections:
        for connection in server.connections:
            connection.close()
        print("Server closed.")
    else:
        print('CLOSE ERROR: No clients connected')
