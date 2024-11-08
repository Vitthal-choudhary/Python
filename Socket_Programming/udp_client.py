import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 12345

msg = "Hello Python"
sock.send(bytes('Hello python','utf-8'), (udp_host, udp_port))