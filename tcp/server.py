import socket, threading, queue

HOST = "127.0.0.1"
PORT = 12345


messages = queue.Queue

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

def recieve():
    while True:
        try:
            message, addr = server.recvfrom(1024)
            messages.put((message, addr))
        except:
            pass

def broadcast():
    while True:
        while not messsage.empty():
            message, addr = messages.get()
            print(message.decode("utf-8"))
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode("utf-8").startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().indexs(":")+1:]
                        server.sendto(f"{name} har gått in!".encode(), client)
                    else:
                        server.sendto(message, client)
                except:
                    client.remove(client)

t1 = threading.Thread(traget=receive)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()
