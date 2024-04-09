import socket, threading

class ClientChatroom:
    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.message_log: list[bytes] = []

        self.is_alive = True
        def receive():
            while self.is_alive:
                data = self.sock.recv(1024)
                if not data: 
                    print("THIS CHAT HAS BEEN TERMINATED")
                    self.is_alive = False
                    break
                print(data)
                self.message_log.append(data)

        self.receive_thread = threading.Thread(target=receive)
        self.receive_thread.start()

    def terminate(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        self.is_alive = False

    def send(self, message):
        self.message_log.append(message)
        self.sock.sendall(message)

