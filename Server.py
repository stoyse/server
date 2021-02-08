import socket
import threading
from art import *
import time
import os

welcome_print = text2art("stosse-server")
online_print = text2art("stosse-server online")

print(welcome_print)
time.sleep(2)

os.system('ifconfig')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 777))
server_socket.listen(10)

print(online_print)

while True:
    (client_socket, client_addr) = server_socket.accept()
    print(f'Client {client_addr} connected | {client_socket}')
    rec_msg = client_socket.recv(1024)
    print(str(msg, 'utf8'))