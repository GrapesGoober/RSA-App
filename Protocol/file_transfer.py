import socket, RSA
from typing import Generator, Iterable

# sets up a TCP server, exchange key modulus, and receives data
def receive_stream(ip: str, port: int, keys: tuple[int, int]) -> Generator[bytes, None, None]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen()
    conn, addr = sock.accept()
    print(f"connected from {addr}")
    k_priv, modulus = keys
    conn.sendall(modulus.to_bytes(modulus.bit_length() // 8 + 1))
    while data := conn.recv(1024):
        yield RSA.decrypt(data, (k_priv, modulus))

# connects to TCP server, exchange key modulus, and sends data
def send_data(ip: str, port: int, data: bytes):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip, port))
    key_n = int.from_bytes(conn.recv(1024))
    encrypted = RSA.encrypt(data, (65537, key_n))
    conn.sendall(encrypted)
    conn.close()

