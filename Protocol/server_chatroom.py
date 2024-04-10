import select, socket, threading

messages = [ ] # outgoing message queue
is_running = False
sock: socket.socket = None
select_inout = [ ]

def start_chatroom(ip: str, port: int):
    global sock, is_running
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.bind((ip, port))
    sock.listen()
    select_inout.append(sock)
    is_running = True
    chatroom = threading.Thread(target=chatroom_thread)
    chatroom.start()

def chatroom_thread():
    while is_running:
        readable, writable, _ = select.select(select_inout, select_inout, [])
        for s in readable:
            if s is sock:
                conn, addr = s.accept()
                print(f"connected from {addr}")
                select_inout.append(conn)
            else: 
                data = s.recv(1024)
                if data:
                    print(data)
                if not data:
                    print("THIS CHATROOM IS TERMINATED")
                    sock.close()
                    return
        for s in writable:
            if messages:
                s.sendall(messages[0]) 
                messages.pop(0)
    sock.close()