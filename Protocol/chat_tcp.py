import select, socket, threading

# start a server and await a connection, then returns a connection socket
def start_server(ip: str, port: int) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen()
    conn, addr = sock.accept()
    print(f"connected from {addr}")
    return conn

# connects to a chat server and returns the connection socket
def connect_server(ip: str, port: int) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print(f"connected to {(ip, port)}")
    return sock

def start_chat_sync(conn: socket.socket, to_send: list[bytes], to_receive: list[bytes]):
    sockets = [conn]
    def sync_thread():
        while True:
            readable, writable, _ = select.select(sockets, sockets, [])
            conn: socket.socket
            for conn in readable:
                data = conn.recv(1024)
                to_receive.append(data)
            for conn in writable:
                while to_send:
                    conn.sendall(to_send.pop(0))
    threading.Thread(target=sync_thread).start()


