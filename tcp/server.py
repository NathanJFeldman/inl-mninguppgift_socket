import socket, threading

HOST = "127.0.0.1"
PORT = 12345

chatters : list = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(10)
    