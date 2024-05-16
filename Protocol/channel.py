# this is similiar to file transfer protocol, but this can handle variable data sizes
import socket, RSA
from cryptography.fernet import Fernet
from Protocol.getkeys import get_private_key, get_public_key

class Receiver:
    def __init__(self, ip: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.rsa_key = get_private_key()

    def __enter__(self):
        self.sock.listen()
        self.conn, addr = self.sock.accept()
        ssk_exchange = self.conn.recv(1024)
        self.fernet_ssk = RSA.decrypt(ssk_exchange, self.rsa_key)
        self.fernet = Fernet(self.fernet_ssk)
        return self
    
    def __exit__(self, e_type, e_val, traceback):
        self.conn.close()

    def get_message(self) -> bytes:
        bufsize = int.from_bytes(self.conn.recv(2)) # limit buf size to 65KB
        if not bufsize: return None
        data = self.conn.recv(bufsize)
        return self.fernet.decrypt(data)

class Sender:
    def __init__(self, ip: str, port: int, dest_name: str) -> None:
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = (ip, port)
        self.fernet_ssk = Fernet.generate_key()
        self.fernet = Fernet(self.fernet_ssk)
        self.dest_name = dest_name

    def __enter__(self):
        self.conn.connect(self.host)
        public_key = get_public_key(self.dest_name)
        if not public_key:
            raise Exception(f"Username '{self.dest_name}' does not exist")
        ssk_exchange = RSA.encrypt(self.fernet_ssk, public_key)
        self.conn.sendall(ssk_exchange)
        return self
    
    def __exit__(self, e_type, e_val, traceback):
        self.conn.sendall(b'\0')
        self.conn.close()
    
    def send(self, message: bytes) -> None:
        token = self.fernet.encrypt(message)

        size = len(token)
        if size > 0xFFFF:
            half = len(message) // 2
            self.send(message[:half])
            self.send(message[half:])
        else:
            self.conn.sendall(size.to_bytes(length=2))
            self.conn.sendall(token)


