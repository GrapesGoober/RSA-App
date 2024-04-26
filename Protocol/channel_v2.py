# this is similiar to file transfer protocol, but this can handle variable data sizes
import socket, RSA
from typing import Generator
from cryptography.fernet import Fernet

class Receiver:
    def __init__(self, ip: str, port: int, keys: tuple[int, int]) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.keys = keys
        self.fernet_ssk = Fernet.generate_key()
        self.fernet = Fernet(self.fernet_ssk)

    def __enter__(self):
        self.sock.listen()
        self.conn, addr = self.sock.accept()
        # let's try using only AES for now
        # _, modulus = self.keys
        # self.conn.sendall(modulus.to_bytes(modulus.bit_length() // 8 + 1))

        self.conn.sendall(self.fernet_ssk)
        return self
    
    def __exit__(self, e_type, e_val, traceback):
        # once the receiver is exited, close connection
        self.conn.close()

    def get_message(self) -> bytes:
        # try getting some data, if so decrypts
        bufsize = int.from_bytes(self.conn.recv(2)) # limit buf size to 65KB
        if not bufsize: return None
        data = self.conn.recv(bufsize)
        return self.fernet.decrypt(data)

class Sender:
    def __init__(self, ip: str, port: int) -> None:
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = (ip, port)

    def __enter__(self):
        self.conn.connect(self.host)
        self.fernet_ssk = self.conn.recv(44) # fernet uses 44 bytes key
        self.fernet = Fernet(self.fernet_ssk)
        return self
    
    def __exit__(self, e_type, e_val, traceback):
        self.conn.sendall(b'\0')
        self.conn.close()
    
    def send(self, message: bytes) -> None:
        token = self.fernet.encrypt(message)
        size = len(token)
        if size > 0xFFFF: raise Exception("Message too big!")
        self.conn.sendall(size.to_bytes(length=2))
        self.conn.sendall(token)


