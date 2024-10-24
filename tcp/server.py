import socket, threading

HOST = "127.0.0.1"
PORT = 12345

chatters : list = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(10)

    def chat_joined():
        print("{addr} has connected.")
        chatters.append(sock)
        while True:
            try:
                message = sock.recv(1024).decode("utf-8")
                if message:
                    send_all(message, sock)
            except:
                break



    def send_all(message, sender):
        for chatter in chatters:
            if chatter != sender:
                try:
                    chatter.send(message.encode("utf-8"))
                except:
                    sock.close()
                    chatters.remove(chatter)
    def 