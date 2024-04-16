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
    _, cipher_text_block_size = RSA.get_block_size(modulus)
    # buffer size should match up to the RSA block size
    buffer = cipher_text_block_size * 4
    entire_data = []
    while data := conn.recv(buffer):
        entire_data.append(data)
    entire_data = b"".join(entire_data)
    yield RSA.decrypt(entire_data, (k_priv, modulus))

# connects to TCP server, exchange key modulus, and sends data
def send_data(ip: str, port: int, data: bytes):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip, port))
    modulus = int.from_bytes(conn.recv(1024))
    encrypted = RSA.encrypt(data, modulus)
    conn.sendall(encrypted)
    conn.close()
