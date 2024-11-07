import socket
import threading
import queue

HOST = "127.0.0.1"
PORT = 44444

# Initialize message queue and clients list
messages = queue.Queue()  #type: ignore
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3) # Set the socket option to allow reuse of local addresses
server.bind((HOST, PORT)) # Bind the socket to the local address and port

def receive():
    while True:
        try:
            message, addr = server.recvfrom(1024)  # Receive message from a client
            messages.put((message, addr))  # Add message to queue
        except Exception as e:
            print(f"Problem med att få meddelandet: {e}")

def broadcast():
    while True:
        if not messages.empty():  # Only process if there are messages in the queue
            message, addr = messages.get()  # Get message from queue
            print(f"Meddelandet har skickats in: {message.decode('utf-8')} from {addr}")

            if addr not in clients:
                clients.append(addr) # adds client to the clients list

            for client in clients:
                try:
                    if message.decode("utf-8").startswith("valt_namn:"): # client chooses a name
                        name = message.decode()[message.decode().index(":") + 1:] # name gets index with the format "name":"message"
                        server.sendto(f"{name} har gått in!".encode(), client) # server sends this message to the clients
                    else:
                        server.sendto(message, client)  # Broadcast message to all clients
                except Exception as error: # checks for errors
                    print(f"Error sending message to {client}: {error}")
                    if client in clients: # if there is an error the server removes the client from the server
                        clients.remove(client)

# Start the receive and broadcast threads
t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()

try:
    while True:
        pass  # Keep the main thread alive
except KeyboardInterrupt:
    print("Server shutting down...")
    server.close()
