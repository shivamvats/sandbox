import socket
from time import sleep

HOST = '127.0.0.1'
PORT = 54000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(10):
        s.sendall(b'Hello World')
        sleep(1)

