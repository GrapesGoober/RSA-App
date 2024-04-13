import socket, RSA
from typing import Generator, Iterable

# sets up a TCP server, exchange key modulus, and receives data
def receive_stream(ip: str, port: int, key: int) -> Generator[int, None, None]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen()
    conn, addr = sock.accept()
    print(f"connected from {addr}")
    conn.sendall(key.to_bytes(key.bit_length() // 8 + 1))
    print(f"key sent")

# connects to TCP server, exchange key modulus, and sends data
def send_stream(ip: str, port: int, data: Iterable[bytes]):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip, port))
    print(f"connected to {(ip, port)}")
    key_n = int.from_bytes(conn.recv(1024))
    print(f"key received")
    print(key_n)
