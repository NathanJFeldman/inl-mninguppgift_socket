import socket, select, sys

HOST = "127.0.0.1"
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        chat : str = input("Enter: ")
        encoded_data = chat.encode("utf-8")
        sent_message = "{addr}: {encoded_data}"
        sock.sendto(encoded_data, (HOST, PORT))
        decoded_message = data.decode("utf-8")




    #print("Connected")
    #sock.connect((HOST, PORT))
    #message = "Welcome to the chat"
    #encoded_message = message.encode("utf-8")
    #sock.sendall(encoded_message)
    #chat = pyip.inputStr("Type in chat: ")
#
    #response = sock.recv(512)

#decoded_response = response.decode("utf-8")
#print(f"svaret från clientsockn: {decoded_response}") 