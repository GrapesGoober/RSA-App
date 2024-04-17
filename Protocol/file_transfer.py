import socket, RSA

# sets up a TCP server, awaits connection, and exchange key modulus
def await_conn(ip: str, port: int, keys: tuple[int, int]) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen()
    conn, addr = sock.accept()
    _, modulus = keys
    conn.sendall(modulus.to_bytes(modulus.bit_length() // 8 + 1))
    return conn, addr

# receives data and decrypts
def receive_and_decrypt(conn: socket.socket, keys: tuple[int, int]) -> bytes:
    buf_list: list[bytes] = []
    while buf := conn.recv(1024): buf_list.append(buf)
    return RSA.decrypt(b''.join(buf_list), keys)

# connects to TCP server, exchange key modulus, and sends data
def send_data(ip: str, port: int, data: bytes):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip, port))
    modulus = int.from_bytes(conn.recv(1024))
    encrypted = RSA.encrypt(data, modulus)
    conn.sendall(encrypted)
    conn.close()
