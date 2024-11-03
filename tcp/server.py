import socket, threading

HOST = "127.0.0.1"
PORT = 12345

clients : list = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Enable broadcasting mode
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def hantera_client(client):
        while True:
            try:
                message = client.recv(1024)
                for client in clients:
                    client.send(message)

            except:
                clients.remove(client)
    def chat_room():
        s.bind((HOST, PORT))
        s.listen(2)
        client, adress = s.accept()
        while True:
            print(f"Connected with: {adress}")
            thread = threading.Thread(target=hantera_client, args=(client,))
            thread.start()
    chat_room()
