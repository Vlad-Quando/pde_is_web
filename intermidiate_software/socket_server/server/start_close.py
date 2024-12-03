def start(server):
    '''Starts the loop of awaiting of clients'''
    
    # Server loop
    while True:
        try:

            connection, address = server.socket.accept()        # Establishing a connection
            server.connections.append((connection, address))    # Adding the connection to connections list
            print("Connected to", address, connection)          # Printing message 
        except Exception as e:
            print("Error while starting accepting clients loop:", e)
            break


def close(server):
    '''Shuts down the server and closes all connections'''

    if server.connections:                      # If there are connections
        for connection in server.connections:   # Running though connections list
            connection.close()                  # Closing all connections
        print("Server closed.")                 # Printing message about it
    else:
        print('CLOSE ERROR: No clients connected')
