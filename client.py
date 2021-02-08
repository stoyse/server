import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('192.168.178.47', 777)
client_socket.connect(server_addr)
client_socket.send(bytes('Hello', 'utf8'))