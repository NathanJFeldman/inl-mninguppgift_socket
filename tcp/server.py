import socket, sys, select

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    print(f"server is listening on socket address: {HOST}:{PORT}")
    sock.listen(10)
    chatters : list = []
    def chat(conn, addr):
        conn, addr = sock.accept()
        with conn:
            print(f"connection establied: {conn}\n")
            print(f"Welcome to the chatroom!")
            while True:
                message = conn.recv(2048)
                if message:
                    print(addr[0] + message)
                    message_all = addr[0] + message
                    send_all(message_all, conn)

    def send_all(message, connection):
        for chatter in chatters:
            if chatter != connection:
                try:
                    chatter.send(message)
                except:
                    chatter.close()
    def chat_room(conn, addr, server):
        while True:
            conn, addr = server.accept()
            chatters.append(conn)       
            print(addr[0] + "connected")