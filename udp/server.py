import socket
import threading
import queue

HOST = "127.0.0.1"
PORT = 44444

# Initialize message queue and clients list
messages = queue.Queue()  #type: ignore
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

def receive():
    while True:
        try:
            message, addr = server.recvfrom(1024)  # Receive message from a client
            messages.put((message, addr))  # Add message to queue
        except Exception as e:
            print(f"Error receiving message: {e}")

def broadcast():
    while True:
        if not messages.empty():  # Only process if there are messages in the queue
            message, addr = messages.get()  # Get message from queue
            print(f"Received message: {message.decode('utf-8')} from {addr}")

            if addr not in clients:
                clients.append(addr)

            for client in clients:
                try:
                    if message.decode("utf-8").startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":") + 1:]
                        server.sendto(f"{name} har gått in!".encode(), client)
                    else:
                        server.sendto(message, client)  # Broadcast message to all clients
                except Exception as e:
                    print(f"Error sending message to {client}: {e}")
                    if client in clients:
                        clients.remove(client)

# Start the receive and broadcast threads
t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()