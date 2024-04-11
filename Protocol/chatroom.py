import select, socket

messages:   list[bytes] = []
server =    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets:    list[socket.socket] = [server]
users:      dict[socket.socket, dict] = {}

# Persistent TCP
def start_chatroom(ip: str, port: int):
    server.setblocking(False)
    server.bind((ip, port))
    server.listen(2)
    while True:
        readable: list[socket.socket]
        readable, _, _ = select.select(sockets, [], [])
        for s in readable:
            if s is server:     # server receives a new user connection
                conn, addr = s.accept()
                print(f"connected from {addr}")
                sockets.append(conn)
                users[conn] = {"addr": addr}
            elif conn := s:     # connection receives new data
                data = None
                try: data = conn.recv(1024)
                except ConnectionResetError: pass
                if data: print(data)
                else: handle_disconnected_user(conn)

def handle_disconnected_user(conn: socket.socket):
    print(f"user {users[conn] } disconnects")
    conn.close()
    sockets.remove(conn)

