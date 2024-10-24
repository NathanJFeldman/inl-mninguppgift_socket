import socket, select, sys

HOST = "127.0.0.1"
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        chat : str = input("Enter: ")
        data, addr = sock.recvfrom(2048)
        encoded_data = chat.encode("utf-8")
        sent_message = "{addr}: {encoded_data}"
        sock.sendto(encoded_data, (HOST, PORT))
        decoded_message = data.decode("utf-8")
        


