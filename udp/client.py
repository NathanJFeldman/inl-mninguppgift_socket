import socket, threading, queue

HOST = "127.0.0.1"
PORT = 44444

# Create a UDP socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the local address and port
client.bind((HOST, PORT))

# Prompt the user to enter their name
name = input("Skriv vad du heter: ")

# Function to receive and print messages from the server
def receive():
    while True:
        try:
            # Receive a message from the server (with a max buffer size of 1024 bytes)
            message, _ = client.recvfrom(1024)
            # Decode and print the received message
            print(message.decode())
        except:
            # If an error occurs, just pass (e.g., socket disconnect)
            pass

# Start a new thread to handle receiving messages
t = threading.Thread(target=receive)
t.start()

# Send the user's name to the server as the initial message
client.sendto(f"valt_namn:{name}".encode(), (HOST, PORT))

# Main loop to send messages to the server
while True:
    # Prompt the user to input a message
    message = input("Enter a message: ")
    
    # If the user types "exit", exit the program
    if message == "exit":
        exit()
    else:
        # Send the user's message to the server, prepended with the user's name
        client.sendto(f"{name}: {message}".encode(), (HOST, PORT))
