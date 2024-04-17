import socket, RSA
from typing import Generator


# sets up a TCP server, exchange key modulus, and receives data
def receive_data(ip: str, port: int, keys: tuple[int, int]) -> Generator[bytes, None, None]:

    # create server and await connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen()
    conn, addr = sock.accept()
    print(f"connected from {addr}")

    # exchange key modulus
    _, modulus = keys
    conn.sendall(modulus.to_bytes(modulus.bit_length() // 8 + 1))

    # receive data, using a bytes list as buffer
    print(f"receiving data")
    buf_list: list[bytes] = []
    while buf := conn.recv(1024): buf_list.append(buf)
    print(f"decrypting")
    return RSA.decrypt(b''.join(buf_list), keys)

# connects to TCP server, exchange key modulus, and sends data
def send_data(ip: str, port: int, data: bytes):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip, port))
    modulus = int.from_bytes(conn.recv(1024))
    encrypted = RSA.encrypt(data, modulus)
    conn.sendall(encrypted)
    conn.close()
