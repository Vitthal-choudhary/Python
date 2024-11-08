import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 14253

sock.bind((udp_host, udp_port))
print("Waiting For client :....")

while True:
    client, address = sock.recvfrom(1024)
    print("Connected to ", address)
    print("Recieved Messages: ", client.recv(1024).decode(), "from", address)