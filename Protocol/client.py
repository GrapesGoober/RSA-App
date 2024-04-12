import socket, time                                                                                                                          

CHAT_TYPE = b"CHAT"
SYNC_TYPE = b"SYNC"

class ClientChatroom:
    messages:   list[bytes] = []
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self, ip: str, port: int):
        self.client.connect((ip, port))
        self.client.sendall(CHAT_TYPE)

    def send_message(self, message: bytes):
        self.client.sendall(message)

    def disconnects(self):
        self.client.close()

def sync_chatroom(ip: str, port: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.sendall(SYNC_TYPE)
    print("start syncing...")
    while True:
        data = client.recv(1024)
        print(data)

