import socket


def init_server(server, address, host, port):
	'''Creates a TCPServer object'''

	try:
		server.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creating socket
		
		server.socket.bind(address) 										# Binding socket to the address

		server.socket.listen(1) 											# Starting socket
		print(f"Socket server is listening on {host}:{port}")				# Printing message that server started

		server.connections = list()											# Creating connections list
	except Exception as e:
		print("Failded to start socket server due to error:", e)
