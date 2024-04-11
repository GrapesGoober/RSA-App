import socket                                                                                                                          

class ClientChatroom:
    messages:   list[bytes] = []
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self, ip: str, port: int):
        self.client.connect((ip, port))

    def send_message(self, message: bytes):
        self.client.sendall(message)

    def disconnects(self):
        self.client.close()