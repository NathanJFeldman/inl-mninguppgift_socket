import socket
import threading
import queue

HOST = "127.0.0.1"
PORT = 44444

# Initialize message queue and clients list
messages = queue.Queue()  # type: ignore
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3)  # Set the socket option to allow reuse of local addresses
server.bind((HOST, PORT))  # Bind the socket to the local address and port

# Flag to control the running status of the server
running = True

def receive():
    global running
    while running:  # Check if the server is running
        try:
            message, addr = server.recvfrom(1024)  # Receive message from a client
            messages.put((message, addr))  # Add message to queue
        except Exception as e:
            print(f"Problem med att få meddelandet: {e}")

def broadcast():
    global running
    while running:  # Check if the server is running
        if not messages.empty():  # Only process if there are messages in the queue
            message, addr = messages.get()  # Get message from queue
            print(f"Meddelandet har skickats in: {message.decode('utf-8')} from {addr}")

            if addr not in clients:
                clients.append(addr)  # Adds client to the clients list

            for client in clients:
                try:
                    if message.decode("utf-8").startswith("valt_namn:"):  # Client chooses a name
                        name = message.decode()[message.decode().index(":") + 1:]  # Extract name from message
                        server.sendto(f"{name} har gått in!".encode(), client)  # Server sends this message to clients
                    else:
                        server.sendto(message, client)  # Broadcast message to all clients
                except Exception as error:  # Check for errors
                    print(f"Error sending message to {client}: {error}")
                    if client in clients:  # If there is an error, remove client from list
                        clients.remove(client)

def shutdown_server():
    global running
    # This function is to clean up the server on shutdown
    print("Shutting down server...")
    running = False  # Set the running flag to False to stop threads
    server.close()  # Close the server socket

    # Wait for threads to finish
    t1.join()
    t2.join()
    print("Server shut down successfully.")

# Start the receive and broadcast threads
t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)

t1.start()
t2.start()

try:
    while running:
        pass  # Keep the main thread alive until running is False
except KeyboardInterrupt:
    shutdown_server()  # Cleanly shut down the server on KeyboardInterrupt
