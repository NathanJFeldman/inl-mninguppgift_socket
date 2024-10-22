import socket

HOST = "127.0.0.1"
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    print("Connected")
    client_sock.connect((HOST, PORT))
    print("")

    message = "hello from devops24 demo"
    encoded_message = message.encode("utf-8")

    client_sock.sendall(encoded_message)

    response = client_sock.recv(512)

decoded_response = response.decode("utf-8")
print(f"svaret från servern: {decoded_response}") 