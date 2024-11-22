import socket


def init_server(server, address, host, port):
	'''Creates a TCPServer object'''

	server.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating socket
	
	server.socket.bind(address) # Binding socket to the address

	server.socket.listen(1) # Starting socket
	print(f"Socket server is listening on {host}:{port}")

	server.connection = None
	server.address = None
