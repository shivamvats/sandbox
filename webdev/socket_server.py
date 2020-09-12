import socket

"""This script launches a server that listens to a local port and prints the
input."""

HOST = '127.0.0.1'
PORT = 54000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    # Make s a listening socket
    s.listen()
    # Wait for a connection
    # The connection is established over another socket
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        # Keep listening to the client
        while True:
            data = conn.recv(1024) # Max read size
            if not data:
                break
            print(data)
            print('\n')

