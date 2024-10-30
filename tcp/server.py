import socket, threading

HOST = "127.0.0.1"
PORT = 12345

chatters : list = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def client_handle():
    while True:
        data = server.recvfrom(1024)
        if not data:
            break
        message = data.decode("utf-8")
        response = "<{addr}>" + message
        server.sendall(response.encode("utf-8"))

def chat_room():

    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Connected to: {HOST}:{PORT}")

    while True:
        data, addr = server.accept()
        print(f"Client connected from {addr}")

        

if __name__ == "__main__":
    chat_room()

