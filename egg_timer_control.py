#!/usr/bin/env python3
import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65441        # The port used by the server

if(len(sys.argv) > 1):
    command = sys.argv[1]
else:
    command = 'toggle_play'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytearray(command, 'utf-8'))


