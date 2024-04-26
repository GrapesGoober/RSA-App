# this is similiar to file transfer protocol, but this can handle variable data sizes
import socket, RSA
from typing import Generator
from cryptography.fernet import Fernet

class Receiver:
    def __init__(self, ip: str, port: int, rsa_key: tuple[int, int]) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.rsa_key = rsa_key

    def __enter__(self):
        self.sock.listen()
        self.conn, addr = self.sock.accept()

        _, modulus = self.rsa_key
        modulus = modulus.to_bytes(modulus.bit_length() // 8 + 1)
        self.conn.sendall(modulus)
        ssk_exchange = self.conn.recv(1024)
        self.fernet_ssk = RSA.decrypt(ssk_exchange, self.rsa_key)
        self.fernet = Fernet(self.fernet_ssk)

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
        self.fernet_ssk = Fernet.generate_key()
        self.fernet = Fernet(self.fernet_ssk)

    def __enter__(self):
        self.conn.connect(self.host)
        modulus = int.from_bytes(self.conn.recv(1024))
        ssk_exchange = RSA.encrypt(self.fernet_ssk, modulus)
        self.conn.sendall(ssk_exchange)
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


