import socket, threading

HOST = "127.0.0.1"
PORT = 12345

clients : list = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.close()

def send_messages(message):
    for client in clients:
        client.send(message)

def hantera_client(client):
    while True:
        try:
            message = client.recv(1024)
            send_messages(message)
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

if __name__ == "__main__":
    chat_room() 