import select, socket, threading

to_send:    list[bytes] = []
received:   list[bytes] = []
sockets:    list[socket.socket] = []

# start a server and await a connection, then returns a connection socket
def start_server(ip: str, port: int) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen()
    conn, addr = sock.accept()
    print(f"connected from {addr}")
    sockets.append(conn)

# connects to a chat server and returns the connection socket
def connect_server(ip: str, port: int) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print(f"connected to {(ip, port)}")
    sockets.append(sock)

def start_chat_sync():
    def sync_thread():
        while True:
            readable, writable, _ = select.select(sockets, sockets, [])
            for conn in readable:   recv_message(conn)
            for conn in writable:   send_message(conn)
    threading.Thread(target=sync_thread).start()

# handle a case where connection receives new data
def recv_message(conn: socket.socket):
    data: bytes = None
    try: data = conn.recv(1024)
    except ConnectionResetError: pass
    if data: received.append(data)
    else: 
        sockets.remove(conn)
        conn.close()

# send the received messages to sync clients
def send_message(conn: socket.socket):
    while to_send:
        try: conn.sendall(to_send.pop(0))
        except ConnectionResetError: 
            sockets.remove(conn)
            conn.close()

