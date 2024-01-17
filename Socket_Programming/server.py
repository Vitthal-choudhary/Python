import socket
import threading        #threading helps us to run other code while other is waiting

HEADER = 64
PORT = 5050
#Server = "192.168.56.1" # instead we use
SERVER = socket.gethostbyname(socket.gethostname())     #gets ip address of this local machine
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!! DISCONNECT !!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def handle_connection(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg recieved".encode(FORMAT))
    conn.close()


def start():
    print(f"[LISTENING] on {SERVER}")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE  CONNECTIONS] {threading.active_count()-1}")


print("[SERVER] is starting ..........")
start()