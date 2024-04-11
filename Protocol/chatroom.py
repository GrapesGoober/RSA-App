from Protocol.keys import Apriv, Apub, Bpriv, Bpub
import select, socket

messages:   list[bytes] = []
server =    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets:    list[socket.socket] = [server]

def start_chatroom(ip: str, port: int):
    server.setblocking(False)
    server.bind((ip, port))
    server.listen()
    while True:
        readable: list[socket.socket]
        readable, _, _ = select.select(sockets, [], [])
        for s in readable:
            if s is server: # server receives a new connection
                conn, addr = s.accept()
                print(f"connected from {addr}")
                sockets.append(conn)
            else:           # connection receives new data
                data = s.recv(1024)
                if data: print(data)
                if not data:
                    print(f"user disconnects")
                    s.close()
                    sockets.remove(s)

