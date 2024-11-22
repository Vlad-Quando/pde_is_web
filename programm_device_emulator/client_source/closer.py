def close(client):
    '''Closes the connectio with the server'''
    
    client.socket.close() # Closing connection