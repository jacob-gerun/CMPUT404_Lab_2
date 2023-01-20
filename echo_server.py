import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn,addr):
    # conn is a socket directly to the client 
    # Created by s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)  # b/c this is an echo server
    return

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        # Allows a socket to rebind to the same socket under certain circumstances
        # If you have a socket that you close and it is in the "timeout" stage this lets you rebind
        # Should answer a lab question
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1) 
        s.listen()
        conn, addr = s.accept()
        handle_connection(conn, addr)
    return

start_server()
