import select, socket, time

messages:   list[bytes] = []
server =    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets:    list[socket.socket] = [server]
clients:    dict[socket.socket, dict] = {}

CHAT_TYPE = b"CHAT"
SYNC_TYPE = b"SYNC"

# Persistent TCP
def run_chatroom(ip: str, port: int):
    server.bind((ip, port))
    server.listen()
    while True:
        readable, writable, _ = select.select(sockets, sockets, [])
        for s in readable:
            if s is server:     handle_new_conn(s) 
            else:               handle_new_data(s)
        for conn in writable:   handle_sync(conn)

# handle a case where server receives a new user connection
def handle_new_conn(server: socket.socket):
    conn, addr = server.accept()
    conn.settimeout(5)  # 5 seconds for client to send their info
    conn_type = conn.recv(1024)
    clients[conn] = {'type': conn_type, 'sync': 0}
    conn.setblocking(False)
    sockets.append(conn)

# handle a case where connection receives new data
def handle_new_data(conn: socket.socket):
    data: bytes = None
    try: data = conn.recv(1024)
    except ConnectionResetError: pass
    if data: messages.append(data)
    else: 
        sockets.remove(conn)
        conn.close()
        clients.pop(conn)

# send the received messages to sync clients
def handle_sync(conn: socket.socket):
    if conn not in clients: return
    if clients[conn]['type'] != SYNC_TYPE: return
    starts_from = clients[conn]['sync']
    for m in messages[starts_from:]:
        conn.sendall(m)
    clients[conn]['sync'] = len(messages)
