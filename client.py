import socket

HEADER = 64
PORT = 5050
STD_FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = "!DISCONNECTED"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(STD_FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(STD_FORMAT)

    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(STD_FORMAT))


send('Hello World!')
