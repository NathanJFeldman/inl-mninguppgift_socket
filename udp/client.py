import socket, threading, queue

HOST = "127.0.0.1"
PORT = 44444

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((HOST, PORT))

name = input("Skriv vad du heter: ")

def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

t = threading.Thread(target=receive)

t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), (HOST, PORT))

while True:
    message = input("")
    if message == "exit":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), (HOST, PORT))
