# this is similiar to file transfer protocol, but this can handle variable data sizes
import socket, RSA
from typing import Generator

class Receiver:
    def __init__(self, ip: str, port: int, keys: tuple[int, int]) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.keys = keys

    def __enter__(self):
        self.sock.listen()
        self.conn, addr = self.sock.accept()
        _, modulus = self.keys
        self.conn.sendall(modulus.to_bytes(modulus.bit_length() // 8 + 1))
        return self
    
    def __exit__(self, e_type, e_val, traceback):
        # once the receiver is exited, close connection
        self.conn.close()

    def get_message(self) -> Generator[bytes, None, None]:
        # try getting some data, if so decrypts
        header = self.conn.recv(2) # limit buf size to 65KB
        if not header: return None
        size = int.from_bytes(header)
        data = self.conn.recv(size)
        return RSA.decrypt(data, self.keys)

class Sender:
    def __init__(self, ip: str, port: int) -> None:
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = (ip, port)

    def __enter__(self):
        self.conn.connect(self.host)
        self.modulus = int.from_bytes(self.conn.recv(1024))
        return self
    
    def __exit__(self, e_type, e_val, traceback):
        self.conn.sendall(b'\0')
        self.conn.close()
    
    def send(self, message: bytes) -> None:
        for pos in range(0, len(message), 0xFFFF):
            chunk = message[pos:pos + 0xFFFF]
            data = RSA.encrypt(chunk, self.modulus)
            self.conn.sendall(len(data).to_bytes(length=2))
            self.conn.sendall(data)


