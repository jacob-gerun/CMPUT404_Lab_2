import socket

BYTES_TO_READ = 4096

def get(host,port):
    request_data = b"GET / HTTP/1.1\nHost: " + host.encode("utf-8") + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(request_data)
    s.shutdown(socket.SHUT_WR) # Shuts down the right end of the socket, eg can still recieve
    result = s.recv(BYTES_TO_READ)
    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)
    s.close()
get("www.google.com",80) # Port 80 is the accepted port standard for HTTP request_data that are not encrypted