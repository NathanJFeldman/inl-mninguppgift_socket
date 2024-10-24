import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    print(f"server is listening on socket address: {HOST}:{PORT}")
    sock.listen(10)

    


    conn, addr = sock.accept()
    with conn:
        print(f"connection establied: {conn}\n")
        print(f"Welcome to the chatroom!")
        while True:
            message = conn.recv(2048)
            if message:
                print(addr[0])
            