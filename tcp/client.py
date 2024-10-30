import socket, threading

HOST = "127.0.0.1"
PORT = 12345

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))
    while True:
        message = input("Enter message -> ")
        server.sendall(message.encode("utf-8"))
        data = server.recv(1024)
        response = data.decode("utf-8")
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()
