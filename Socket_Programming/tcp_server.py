import socket

s = socket.socket()
host = socket.gethostname()
port = 9998

s.bind((host,port))

print("Waiting for Connection")
s.listen(3)

while True:
	conn, addr = s.accept()
	print("Got connection from ", addr)
	conn.send(bytes('Server Saying Hi', 'utf-8'))
	conn.close()