import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
STD_FORMAT_CONVERSION = 'utf-8'

START_STATUS_MSG = "[STARTING] server is starting..."
DISCONNECTED_MESSAGE = "!DISCONNECTED"
STD_LISTENING_MESSAGE = f"[LISTENING] Server is listening on {SERVER}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True

    while connected:
        msg_lenght = conn.recv(HEADER).decode(STD_FORMAT_CONVERSION)

        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(STD_FORMAT_CONVERSION)

            if msg == DISCONNECTED_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send('Msg received'.encode(STD_FORMAT_CONVERSION))

    conn.close()

def start() -> int:
    server.listen()
    print(STD_LISTENING_MESSAGE)

    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print(START_STATUS_MSG)
start()
