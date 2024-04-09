import socket, threading, RSA

class SocketUDP:
    def __init__(self, my_IP: str, my_port: int, dest_IP: str, dest_port: int):
        self.my_IP: str = my_IP
        self.my_port: int = my_port
        self.dest_IP: str = dest_IP
        self.dest_port: int = dest_port
        self.message_log: list[bytes] = []
        self.encrypt_key: tuple[int, int] = None
        self.decrypt_key: tuple[int, int] = None

    def create_sockets(self):
        self.receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receive_sock.bind((self.my_IP, self.my_port))
        self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.receive_thread_is_running = True
        def receive():
            while self.receive_thread_is_running:
                data, addr = self.receive_sock.recvfrom(2048) # buffer size is 2048 bytes
                self.message_log.append(data)

        self.receive_thread = threading.Thread(target=receive)
        self.receive_thread.start()

    def print_log(self):
        for m in self.message_log: print(m)

    def send(self, message: bytes):
        self.send_sock.sendto(message, (self.dest_IP, self.dest_port))
        self.message_log.append(message)

    def terminate(self):
        self.receive_thread_is_running = False

    
