import socket
import pyinputplus as pyip #type: ignore

HOST = "127.0.0.1"
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:





    #print("Connected")
    #client_sock.connect((HOST, PORT))
    #message = "Welcome to the chat"
    #encoded_message = message.encode("utf-8")
    #client_sock.sendall(encoded_message)
    #chat = pyip.inputStr("Type in chat: ")
#
    #response = client_sock.recv(512)

#decoded_response = response.decode("utf-8")
print(f"svaret från servern: {decoded_response}") 