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
                if not data: break
                header, message = data[0].to_bytes(), data[1:]
                print(message)
                self.message_log.append(message)
                if header == b"T":
                    print("THIS CHAT HAS BEEN TERMINATED")
                    self.sock.close()
                    break
            self.is_alive = False

        self.receive_thread = threading.Thread(target=receive, daemon=True)
        self.receive_thread.start()

    def terminate(self):
        self.sock.sendall(b"T-")
        self.is_alive = False

    def send(self, message):
        self.message_log.append(message)
        self.sock.sendall(b'M' + message)

