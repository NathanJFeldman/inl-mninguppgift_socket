import socket

HOST = "127.0.0.0"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    print(f"server is listening on socket address: {HOST}:{PORT}")
    sock.listen()


    conn, addr = sock.accept()
    with conn:
        print(f"connection establied: {conn}")
        
        while True:
            data = conn.recv(512)
            if not data:
                break
            decoded_data = data.decode("utf-8")
            print(f"data sent from client: {decoded_data}")
            conn.sendall(data)